import React from 'react';

const guides = [
  {
    name: 'Rajesh Kumar',
    experience: '12 years experience',
    specialty: 'TTD Logistics',
    photo: '/images/guide-rajesh.jpg',
  },
  {
    name: 'Priya Sharma',
    experience: '9 years experience',
    specialty: 'Temple Ritual Protocol',
    photo: '/images/guide-priya.jpg',
  },
  {
    name: 'Sunil Varma',
    experience: '15 years experience',
    specialty: 'VIP and Fast Track Coordination',
    photo: '/images/guide-sunil.jpg',
  },
];

const GuidesSection = () => {
  return (
    <section id="guides" className="bg-white py-16 sm:py-20">
      <div className="max-w-5xl mx-auto px-4">
        <div className="text-center mb-12">
          <h2 className="text-3xl sm:text-4xl font-bold text-blue-900 mb-4">Trusted Tirupati Guides</h2>
          <p className="text-sm sm:text-base text-gray-600">
            Each guide is verified with TTD, licensed, and trained in crowd management, language assistance, and emergency handling.
          </p>
        </div>

        <div className="grid gap-6 sm:grid-cols-3">
          {guides.map((guide) => (
            <div key={guide.name} className="bg-gray-50 border border-gray-100 rounded-3																		
