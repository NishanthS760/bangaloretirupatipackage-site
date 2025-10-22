import React from 'react';

const faqs = [
  {
    question: 'What are the pickup locations and timings in Bangalore?',
    answer:
      'We operate from three primary pickup points: Anand Rao Circle (Majestic), Indiranagar BDA Complex, and KR Puram (Near Railway Station). The bus departs between 11:30 PM and 12:30 AM.',
  },
  {
    question: 'How does the fast track darshan work?',
    answer:
      'Our licensed guide accompanies the group through a specific fast track access point authorised by TTD. You skip the standard queues and proceed directly after security checks.',
  },
  {
    question: 'Which ID proof is required?',
    answer:
      'Every traveller must carry a valid original government ID such as Aadhaar, Voter ID, Passport, or Driving Licence. A copy is recommended for quick verification.',
  },
  {
    question: 'What is your cancellation policy?',
    answer:
      'If you cancel 48 hours before departure, you receive a 90% refund. Cancellations within 48 hours are non-refundable because darshan slots and logistics are pre-booked.',
  },
  {
    question: 'Is Padmavathi Temple visit included and mandatory?',
    answer:
      'Yes. The Padmavathi Temple visit is included and strongly advised before Balaji darshan. Our guide ensures the schedule accommodates both darshans comfortably.',
  },
];

const FAQSection = () => {
  return (
    <section id="faq" className="py-16 sm:py-20 bg-gray-50">
      <div className="max-w-4xl mx-auto px-4">
        <h2 className="text-3xl sm:text-4xl font-bold text-blue-900 text-center mb-8">Frequently Asked Questions</h2>
        <div className="space-y-4">
          {faqs.map((faq) => (
            <details key={faq.question} className="group bg-white rounded-2xl border border-gray-200 shadow-sm">
              <summary className="flex justify-between items-center p-4 cursor-pointer text-base font-semibold text-blue-900">
                {faq.question}
                <span className="text-amber-500 group-open:rotate-45 transition-transform text-xl">+</span>
              </summary>
              <div className="px-4 pb-5 text-sm text-gray-600">{faq.answer}</div>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FAQSection;
