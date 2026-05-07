import useAuth from '../hooks/useAuth';

const HomePage = () => {
  const { user, logout } = useAuth();
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">Welcome to CityServe</h1>
        <p className="text-gray-600 mb-2">Hello, {user?.name}!</p>
        <p className="text-sm text-gray-500 mb-6">Role: {user?.role}</p>
        <button onClick={logout} className="bg-red-500 text-white px-6 py-2 rounded-lg hover:bg-red-600 transition-colors">Logout</button>
      </div>
    </div>
  );
};

export default HomePage;
