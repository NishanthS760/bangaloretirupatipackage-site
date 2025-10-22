import React from 'react';
import { CheckCircle, IndianRupee, PhoneCall } from 'lucide-react';

const inclusions = [
  'Round trip in deluxe AC sleeper bus',
  'Reserved freshen-up rooms with toiletries',
  'Certified guide escorted fast track darshan',
  'Sri Padmavathi Ammavari Temple visit',
  'Breakfast and traditional vegetarian lunch',
  'Two Tirupati Laddu Prasadam per person',
  'Pickup points: Anand Rao Circle, Indiranagar, KR Puram',
  'All toll, parking, and permit charges included',
  'On-trip support helpline',
];

const PackageDetails = () => {
  return (
    <section id="package-details" className="py-16 sm:py-20 bg-white">
      <div className="max-w-6xl mx-auto px-4">
        <div className="text-center mb-12">
          <h2 className="text-3xl sm:text-4xl font-bold text-blue-900 mb-4">Premium Package Inclusions</h2>
          <p className="text-base sm:text-lg text-gray-600">
            Transparent pricing, zero hidden fees, and complete pilgrimage comfort from start to finish.
          </p>
        </div>

        <div className="grid gap-6 sm:grid-cols-[2fr,1fr]">
          <div className="bg-gray-50 rounded-3xl p-6 sm:p-8 border border-gray-100">
            <h3 className="text-xl font-semibold text-blue-900 mb-4">What You Receive</h3>
            <ul className="grid gap-4 sm:grid-cols-2">
              {inclusions.map((item) => (
                <li key={item} className="flex items-start space-x-3">
                  <CheckCircle className="w-5 h-5 text-amber-500 flex-shrink-0" />
                  <span className="text-sm text-gray-700">{item}</span>
                </li>
              ))}
            </ul>
          </div>

          <aside className="rounded-3xl p-6 sm:p-8 bg-gradient-to-b from-blue-900 to-blue-950 text-white flex flex-col justify-between shadow-xl">
            <div>
              <div className="flex items-center space-x-3 mb-6">
                <IndianRupee className="w-8 h-8 text-amber-400" />
                <h3 className="text-xl font-semibold">Transparent Pricing</h3>
              </div>
              <div className="space-y-4">
                <div className="bg-white/10 rounded-2xl p-4">
                  <p className="text-sm text-blue-100 uppercase tracking-wide">Weekday Fare</p>
                  <p className="text-3xl font-bold">₹2500</p>
                </div>
                <div className="bg-white/10 rounded-2xl p-4">
                  <p className="text-sm text-blue-100 uppercase tracking-wide">Weekend Fare</p>
                  <p className="text-3xl font-bold">₹2800</p>
                </div>
              </div>
            </div>

            <div className="mt-6">
              <p className="text-xs text-blue-100 mb-3">Bookings fill quickly. Reserve in advance.</p>
              <a
                href="tel:+919611621938"
                className="flex items-center justify-center space-x-2 bg-amber-500 hover:bg-amber-400 text-blue-900 font-semibold px-6 py-3 rounded-full transition"
              >
                <PhoneCall className="w-5 h-5" />
                <span>Call 9611621938</span>
              </a>
            </div>
          </aside>
        </div>
      </div>
    </section>
  );
};

export default PackageDetails;
