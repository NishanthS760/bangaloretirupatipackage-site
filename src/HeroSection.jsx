import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Star, Shield, PhoneCall, MapPin } from 'lucide-react';

const HeroSection = () => {
  const [availableSeats, setAvailableSeats] = useState(8); // NOTE: Computer-generated placeholder
  const [totalPilgrimsServed, setTotalPilgrimsServed] = useState(15847); // NOTE: Computer-generated placeholder
  const [nextTripDate, setNextTripDate] = useState('Sunday, 27 October'); // NOTE: Computer-generated placeholder

  useEffect(() => {
    const fetchAvailability = async () => {
      try {
        const response = await axios.get('/api/availability');
        setAvailableSeats(response.data.availableSeats);
        setTotalPilgrimsServed(response.data.totalServed);
        setNextTripDate(response.data.nextTripDate);
      } catch (error) {
        console.warn('Availability fetch failed. Using placeholder values.');
      }
    };
    fetchAvailability();
    const interval = setInterval(fetchAvailability, 60000);
    return () => clearInterval(interval);
  }, []);

  return (
    <section id="hero" className="relative w-full min-h-[90vh] md:h-screen overflow-hidden">
      <div className="absolute inset-0">
        <picture>
          <source
            srcSet="/images/tirupati-sunrise-temple-mobile.webp"
            media="(max-width: 768px)"
          />
          <source srcSet="/images/tirupati-sunrise-temple.webp" type="image/webp" />
          <img
            src="/images/tirupati-sunrise-temple.jpg"
            alt="Tirupati Balaji Temple with sunrise glow"
            className="w-full h-full object-cover"
            loading="eager"
          />
        </picture>
        <div className="absolute inset-0 bg-gradient-to-b from-black/70 via-black/40 to-black/80"></div>
      </div>

      <header className="relative z-20">
        <div className="flex items-center justify-between px-4 py-4 sm:px-6 max-w-6xl mx-auto">
          <div className="flex items-center space-x-3 text-white">
            <img
              src="/images/venkateshwara-icon.png"
              alt="Lord Venkateshwara icon"
              className="w-12 h-12 rounded-full border-2 border-amber-400"
            />
            <div>
              <p className="text-lg font-semibold tracking-wide uppercase">TirupatiBalaji.live</p>
              <p className="text-xs text-amber-300">Official Bangalore to Tirupati Pilgrimage Partner</p>
            </div>
          </div>
          <a
            href="tel:+919611621938"
            className="hidden sm:flex items-center space-x-2 bg-green-600 hover:bg-green-700 text-white font-medium px-4 py-2 rounded-full transition"
          >
            <PhoneCall className="w-4 h-4" />
            <span>Call 9611621938</span>
          </a>
        </div>
      </header>

      <div className="relative z-20 max-w-4xl mx-auto px-4 py-16 sm:py-20 text-white text-center">
        <div className="inline-flex items-center space-x-2 bg-white/10 backdrop-blur-md rounded-full px-4 py-2 mb-6 border border-white/20">
          <Star className="w-4 h-4 text-amber-300" />
          <p className="text-sm">
            Rated 4.9/5 by {totalPilgrimsServed.toLocaleString()} verified pilgrims {/* NOTE: Computer-generated placeholder */}
          </p>
        </div>

        <h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold leading-tight mb-4">
          Bangalore → Tirupati Balaji
          <span className="block text-amber-300 mt-2">One Day Express Darshan Package</span>
        </h1>

        <p className="text-base sm:text-lg md:text-xl text-gray-200 mb-8">
          AC Sleeper Bus • Freshen-Up Room • Fast-Track Guided Darshan • Padmavathi Temple Visit • Breakfast and Lunch Included • Laddu Prasadam
        </p>

        <div className="grid gap-4 sm:grid-cols-2 mb-8">
          <div className="bg-black/50 backdrop-blur-md rounded-lg p-4 text-left">
            <p className="text-sm text-gray-300">Next departure</p>
            <p className="text-xl font-semibold">{nextTripDate}</p>
          </div>
          <div className="bg-black/50 backdrop-blur-md rounded-lg p-4 text-left">
            <p className="text-sm text-gray-300">Real-time seats left</p>
            <p className="text-xl font-semibold text-amber-300">{availableSeats}</p>
          </div>
        </div>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-12">
          <button
            onClick={() => document.getElementById('booking-form').scrollIntoView({ behavior: 'smooth' })}
            className="w-full sm:w-auto bg-amber-500 hover:bg-amber-600 text-black font-semibold px-8 py-3 rounded-full transition shadow-lg"
          >
            Reserve Seats Now
          </button>
          <a
            href="#package-details"
            className="w-full sm:w-auto flex items-center justify-center space-x-2 bg-white/10 hover:bg-white/20 text-white px-6 py-3 rounded-full transition"
          >
            <Shield className="w-5 h-5" />
            <span>View Package Inclusions</span>
          </a>
        </div>

        <div className="grid gap-4 sm:grid-cols-2 max-w-xl mx-auto">
          <div className="flex items-center justify-center space-x-2 text-sm sm:text-base text-gray-200">
            <MapPin className="w-5 h-5 text-amber-400" />
            <span>Pickup: Anand Rao Circle • Indiranagar • KR Puram</span>
          </div>
          <div className="flex items-center justify-center space-x-2 text-sm sm:text-base text-gray-200">
            <Shield className="w-5 h-5 text-green-400" />
            <span>Verified guides with 100% safety record</span>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
