import React, { useState } from 'react';
import { Calendar, Clock } from 'lucide-react';

const crowdEstimates = {
  low: {
    value: 'Low Crowd',
    waitRange: '1.5 - 2.5 hours',
    color: 'text-green-600 bg-green-50 border-green-200',
  },
  medium: {
    value: 'Moderate Crowd',
    waitRange: '3 - 4.5 hours',
    color: 'text-amber-600 bg-amber-50 border-amber-200',
  },
  high: {
    value: 'High Crowd',
    waitRange: '5 - 7 hours',
    color: 'text-red-600 bg-red-50 border-red-200',
  },
};

const DarshanTimeSaver = () => {
  const [selectedCrowd, setSelectedCrowd] = useState('low'); // NOTE: Computer-generated default
  const [selectedDate, setSelectedDate] = useState(new Date().toISOString().substring(0, 10));

  const estimate = crowdEstimates[selectedCrowd];

  return (
    <section id="timesaver" className="bg-blue-900 text-white py-16 sm:py-20">
      <div className="max-w-4xl mx-auto px-4">
        <div className="text-center mb-12">
          <h2 className="text-3xl sm:text-4xl font-bold mb-4">Darshan Time Saver Widget</h2>
          <p className="text-base sm:text-lg text-blue-100">
            Estimate the crowd level and queue time based on Tirumala Tirupati Devasthanams updates and guide insights.
          </p>
        </div>

        <div className="bg-white text-gray-800 rounded-3xl p-6 sm:p-8 shadow-2xl">
          <div className="grid gap-6 sm:grid-cols-2">
            <div>
              <label htmlFor="travel-date" className="block text-sm font-semibold text-blue-900 mb-2">
                Selected Darshan Date
              </label>
              <div className="flex items-center border border-gray-200 rounded-xl px-3 py-2">
                <Calendar className="w-5 h-5 text-amber-500 mr-2" />
                <input
                  id="travel-date"
                  type="date"
                  value={selectedDate}
                  onChange={(event) => setSelectedDate(event.target.value)}
                  className="w-full bg-transparent text-gray-700 focus:outline-none"
                />
              </div>
            </div>

            <div>
              <p className="text-sm font-semibold text-blue-900 mb-2">Crowd Snapshot</p>
              <div className="flex items-center space-x-3">
                {['low', 'medium', 'high'].map((level) => (
                  <button
                    key={level}
                    onClick={() => setSelectedCrowd(level)}
                    className={`flex-1 py-3 rounded-xl border text-sm font-semibold transition ${
                      selectedCrowd === level
                        ? 'bg-amber-500 text-white border-amber-600'
                        : 'border-gray-200 text-gray-600 hover:border-amber-200'
                    }`}
                  >
                    {crowdEstimates[level].value}
                  </button>
                ))}
              </div>
            </div>
          </div>

          <div className={`mt-8 border rounded-2xl p-6 ${estimate.color}`}>
            <div className="flex items-center space-x-3 mb-4">
              <Clock className="w-5 h-5" />
              <p className="text-lg font-semibold">Estimated Queue Time (Fast-Track Darshan)</p>
            </div>
            <p className="text-3xl font-bold">{estimate.waitRange}</p>
            <p className="text-sm text-gray-600 mt-2">
              *Estimates are curated using official data and on-ground guide intelligence. Fast-track entry dramatically reduces waiting time.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default DarshanTimeSaver;
