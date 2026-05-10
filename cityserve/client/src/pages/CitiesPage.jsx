import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axiosInstance from '../api/axios';

const CitiesPage = () => {
    const [cities, setCities] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axiosInstance.get('/cities')
            .then(({ data }) => setCities(data.data.cities))
            .catch(console.error)
            .finally(() => setLoading(false));
    }, []);

    if (loading) return <div className="min-h-screen flex items-center justify-center"><div className="w-8 h-8 border-4 border-blue-600 border-t-transparent rounded-full animate-spin" /></div>;

    return (
        <div className="min-h-screen bg-gray-50 py-10 px-4">
            <div className="max-w-5xl mx-auto">
                <h1 className="text-3xl font-bold text-gray-900 mb-2">Choose Your City</h1>
                <p className="text-gray-500 mb-8">Find local shops and services near you</p>
                <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
                    {cities.map((city) => (
                        <Link key={city._id} to={`/cities/${city.slug}`}
                            className="bg-white rounded-xl shadow-sm border border-gray-100 p-6 text-center hover:shadow-md hover:border-blue-200 transition-all group">
                            <div className="text-4xl mb-3">🏙️</div>
                            <h3 className="font-semibold text-gray-800 group-hover:text-blue-600">{city.name}</h3>
                            <p className="text-xs text-gray-400 mt-1">{city.state}</p>
                        </Link>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default CitiesPage;