import User from '../models/User.model.js';
import asyncHandler from '../utils/asyncHandler.js';
import ApiError from '../utils/ApiError.js';
import ApiResponse from '../utils/ApiResponse.js';

const cookieOptions = {
  httpOnly: true,
  secure: process.env.NODE_ENV === 'production',
  sameSite: 'lax',
  maxAge: 7 * 24 * 60 * 60 * 1000,
};

export const register = asyncHandler(async (req, res) => {
  const { name, email, password, phone, role } = req.body;
  const existingUser = await User.findOne({ email });
  if (existingUser) throw new ApiError(409, 'An account with this email already exists');

  const allowedRoles = ['customer', 'vendor'];
  const userRole = allowedRoles.includes(role) ? role : 'customer';

  const user = await User.create({ name, email, password, phone, role: userRole });
  const accessToken = user.generateAccessToken();
  const createdUser = await User.findById(user._id);

  return res.status(201).cookie('accessToken', accessToken, cookieOptions)
    .json(new ApiResponse(201, { user: createdUser, accessToken }, 'Account created successfully'));
});

export const login = asyncHandler(async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email }).select('+password');
  if (!user) throw new ApiError(401, 'Invalid email or password');

  const isPasswordValid = await user.comparePassword(password);
  if (!isPasswordValid) throw new ApiError(401, 'Invalid email or password');
  if (!user.isActive) throw new ApiError(403, 'Your account has been suspended.');

  const accessToken = user.generateAccessToken();
  const loggedInUser = await User.findById(user._id);

  return res.status(200).cookie('accessToken', accessToken, cookieOptions)
    .json(new ApiResponse(200, { user: loggedInUser, accessToken }, 'Logged in successfully'));
});

export const logout = asyncHandler(async (req, res) => {
  return res.status(200).clearCookie('accessToken', { httpOnly: true, sameSite: 'lax' })
    .json(new ApiResponse(200, {}, 'Logged out successfully'));
});

export const getMe = asyncHandler(async (req, res) => {
  return res.status(200).json(new ApiResponse(200, { user: req.user }, 'User profile fetched'));
});

export const updateProfile = asyncHandler(async (req, res) => {
  const { name, phone } = req.body;
  const updatedUser = await User.findByIdAndUpdate(
    req.user._id, { name, phone }, { new: true, runValidators: true }
  );
  return res.status(200).json(new ApiResponse(200, { user: updatedUser }, 'Profile updated successfully'));
});

export const changePassword = asyncHandler(async (req, res) => {
  const { currentPassword, newPassword } = req.body;
  const user = await User.findById(req.user._id).select('+password');
  const isMatch = await user.comparePassword(currentPassword);
  if (!isMatch) throw new ApiError(400, 'Current password is incorrect');
  user.password = newPassword;
  await user.save();
  return res.status(200).json(new ApiResponse(200, {}, 'Password changed successfully'));
});
