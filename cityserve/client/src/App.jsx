import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import ProtectedRoute from './routes/ProtectedRoute';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import HomePage from './pages/HomePage';
import CitiesPage from './pages/CitiesPage';
import ShopsPage from './pages/ShopsPage';
import ShopDetailPage from './pages/ShopDetailPage';
import ManageShopPage from './pages/vendor/ManageShopPage';

const App = () => (
  <BrowserRouter>
    <AuthProvider>
      <Routes>
        {/* Public */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/cities" element={<CitiesPage />} />
        <Route path="/cities/:citySlug" element={<ShopsPage />} />
        <Route path="/shops/:slug" element={<ShopDetailPage />} />

        {/* Protected — any logged in user */}
        <Route element={<ProtectedRoute />}>
          <Route path="/" element={<HomePage />} />
        </Route>

        {/* Vendor only */}
        <Route element={<ProtectedRoute allowedRoles={['vendor', 'admin']} />}>
          <Route path="/vendor/shop" element={<ManageShopPage />} />
        </Route>
      </Routes>
    </AuthProvider>
  </BrowserRouter>
);

export default App;