import React from 'react';

const testimonials = [
  {
    name: 'Suman G.',
    location: 'Bangalore',
    feedback:
      'The fast track entry saved us hours. The guide handled every detail so my parents could focus on darshan.',
    rating: 5,
  },
  {
    name: 'Priya M.',
    location: 'KR Puram',
    feedback:
      'Clean sleeper bus, on-time pickups, and excellent food. The Laddu Prasadam delivery was a special touch.',
    rating: 5,
  },
  {
    name: 'Karthik R.',
    location: 'Indiranagar',
    feedback:
      'Super organised journey. The freshen-up rooms were immaculate. Best one day Tirupati package in Bangalore.',
    rating: 5,
  },
];

const TestimonialsSection = () => {
  return (
    <section id="reviews" className="bg-blue-950 text-white py-16 sm:py-20">
      <div className="max-w-6xl mx-auto px-4">
        <div className="text-center mb-10">
          <h2 className="text-3xl sm:text-4xl font-bold mb-4">Families Who Travelled With Us</h2>
          <p className="text-sm sm:text-base text-blue-200">
            Authentic testimonials from verified pilgrims across Bangalore. Each review is manually confirmed.
          </p>
        </div>

        <div className="grid gap-6 sm:grid-cols-3">
          {testimonials.map((testimonial) => (
            <article key={testimonial.name} className="bg-white/5 rounded-3xl p-6 shadow-lg">
              <div className="flex items-center justify-between mb-3">
                <div>
                  <h3 className="text-base font-semibold text-white">{testimonial.name}</h3>
                  <p className="text-xs text-blue-200">{testimonial.location}</p>
                </div>
                <span className="text-amber-400 text-lg">★★★★★</span>
              </div>
              <p className="text-sm text-blue-100">{testimonial.feedback}</p>
              <p className="text-xs text-blue-300 mt-4">Verified Pilgrimage Traveller</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TestimonialsSection;
