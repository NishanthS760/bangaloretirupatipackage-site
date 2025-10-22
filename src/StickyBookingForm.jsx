import React, { useState } from 'react';
import axios from 'axios';

const StickyBookingForm = () => {
  const [formState, setFormState] = useState({
    fullName: '',
    phoneNumber: '',
    travelDate: '',
    seats: 1,
    idProofType: 'Aadhaar',
  });

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submissionFeedback, setSubmissionFeedback] = useState(null);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormState((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsSubmitting(true);
    setSubmissionFeedback(null);
    try {
      const response = await axios.post('/api/booking', formState);
      setSubmissionFeedback({ type: 'success', message: 'Booking request submitted. Our team will contact you shortly.' });
      setFormState({
        fullName: '',
        phoneNumber: '',
        travelDate: '',
        seats: 1,
        idProofType: 'Aadhaar',
      });
    } catch (error) {
      setSubmissionFeedback({ type: 'error', message: 'Submission failed. Please try again or call 9611621938.' });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <aside
      id="booking-form"
      className="fixed bottom-0 left-0 right-0 z-40 bg-white shadow-xl border-t border-gray-200 md:top-1/2 md:right-6 md:left-auto md:w-96 md:rounded-3xl md:transform md:-translate-y-1/2 md:border md:border-gray-100"
    >
      <div className="p-4 sm:p-6">
        <h3 className="text-lg font-semibold text-blue-900 mb-3 text-center">Reserve Your Tirupati Darshan Seats</h3>
        <form className="space-y-4" onSubmit={handleSubmit}>
          <div>
            <label className="text-sm font-medium text-gray-600 block mb-1">Full Name</label>
            <input
              required
              name="fullName"
              value={formState.fullName}
              onChange={handleChange}
              className="w-full rounded-xl border border-gray-200 px-3 py-2 text-sm bg-gray-50 focus:outline-none focus:ring-2 focus:ring-amber-400"
              placeholder="Your name"
            />
          </div>

          <div>
            <label className="text-sm font-medium text-gray-600 block mb-1">Phone Number</label>
            <input
              required
              name="phoneNumber"
              value={formState.phoneNumber}
              onChange={handleChange}
              className="w-full rounded-xl border border-gray-200 px-3 py-2 text-sm bg-gray-50 focus:outline-none focus:ring-2 focus:ring-amber-400"
              placeholder="9611621938"
              inputMode="tel"
            />
          </div>

          <div>
            <label className="text-sm font-medium text-gray-600 block mb-1">Preferred Travel Date</label>
            <input
              required
              type="date"
              name="travelDate"
              value={formState.travelDate}
              onChange={handleChange}
              className="w-full rounded-xl border border-gray-200 px-3 py-2 text-sm bg-gray-50 focus:outline-none focus:ring-2 focus:ring-amber-400"
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="text-sm font-medium text-gray-600 block mb-1">Seats</label>
              <input
                required
                type="number"
                name="seats"
                value={formState.seats}
                min="1"
                max="10"
                onChange={handleChange}
                className="w-full rounded-xl border border-gray-200 px-3 py-2 text-sm bg-gray-50 focus:outline-none focus:ring-2 focus:ring-amber-400"
              />
            </div>
            <div>
              <label className="text-sm font-medium text-gray-600 block mb-1">ID Proof</label>
              <select
                name="idProofType"
                value={formState.idProofType}
                onChange={handleChange}
                className="w-full rounded-xl border border-gray-200 px-3 py-2 text-sm bg-gray-50 focus:outline-none focus:ring-2 focus:ring-amber-400"
              >
                <option value="Aadhaar">Aadhaar</option>
                <option value="Voter ID">Voter ID</option>
                <option value="Passport">Passport</option>
                <option value="Driving Licence">Driving Licence</option>
              </select>
            </div>
          </div>

          <button
            type="submit"
            disabled={isSubmitting}
            className="w-full bg-amber-500 hover:bg-amber-400 text-blue-900 font-semibold py-3 rounded-full transition disabled:opacity-70 disabled:cursor-not-allowed"
          >
            {isSubmitting ? 'Processing…' : 'Pay 50% Advance to Reserve'}
          </button>

          <p className="text-xs text-gray-500 text-center">
            90% refund if cancelled 48 hours before departure. Full policy shared in booking confirmation.
          </p>

          {submissionFeedback && (
            <div
              className={`text-sm text-center rounded-xl px-4 py-2 ${
                submissionFeedback.type === 'success'
                  ? 'bg-green-50 text-green-700'
                  : 'bg-red-50 text-red-600'
              }`}
            >
              {submissionFeedback.message}
            </div>
          )}
        </form>
      </div>
    </aside>
  );
};

export default StickyBookingForm;
