import React from 'react';
import { Bus, Bed, Coffee, Landmark, Utensils, Camera } from 'lucide-react';

const timelineData = [
  {
    title: 'Pickup from Bangalore',
    time: '11:30 PM - 12:30 AM',
    description:
      'Board from Anand Rao Circle (Majestic), Indiranagar, or KR Puram. Professional crew welcomes you on board.',
    icon: Bus,
  },
  {
    title: 'Overnight AC Sleeper Journey',
    time: '12:30 AM - 5:30 AM',
    description:
      'Recline in sanitized AC sleeper berths. Dedicated drivers ensure a smooth, safe journey to Tirupati.',
    icon: Bed,
  },
  {
    title: 'Freshen Up and Breakfast',
    time: '5:30 AM - 7:00 AM',
    description:
      'Access reserved freshen-up rooms. Enjoy hot South Indian breakfast with coffee and fruits.',
    icon: Coffee,
  },
  {
    title: 'Fast-Track Balaji Darshan',
    time: '7:30 AM - 11:30 AM',
    description:
      'Certified guide orchestrates fast-track entry at Tirumala. Avoid long queues and stay focused on darshan.',
    icon: Landmark,
  },
  {
    title: 'Padmavathi Temple and Lunch',
    time: '12:00 PM - 2:00 PM',
    description:
      'Visit Sri Padmavathi Temple, followed by a wholesome vegetarian lunch with Laddu Prasadam.',
    icon: Utensils,
  },
  {
    title: 'Return Journey to Bangalore',
    time: '2:30 PM - 10:30 PM',
    description:
      'Relax on the return trip. Share photos and memories with fellow pilgrims while we drop you back safely.',
    icon: Camera,
  },
];

const TimelineSection = () => {
  return (
    <section id="journey" className="bg-white py-16 sm:py-20">
      <div className="max-w-6xl mx-auto px-4">
        <h2 className="text-3xl sm:text-4xl font-bold text-center text-blue-900 mb-12">
          Your One Day Pilgrimage Journey
        </h2>
        <div className="grid gap-6 md:grid-cols-3">
          {timelineData.map((step, index) => (
            <div
              key={step.title}
              className="bg-gray-50 border border-gray-200 rounded-2xl p-6 shadow-sm hover:shadow-lg transition transform hover:-translate-y-1"
            >
              <div className="flex items-center space-x-3 mb-4">
                <span className="inline-flex items-center justify-center w-12 h-12 rounded-full bg-amber-100 text-amber-600">
                  <step.icon className="w-6 h-6" />
                </span>
                <h3 className="text-lg font-semibold text-blue-900">{step.title}</h3>
              </div>
              <p className="text-sm text-gray-500 font-medium mb-2">{step.time}</p>
              <p className="text-sm text-gray-700">{step.description}</p>
              <button className="mt-4 text-sm font-semibold text-amber-600 hover:text-amber-700">
                View Details →
              </button>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TimelineSection;
