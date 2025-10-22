import React from 'react';
import HeroSection from './components/HeroSection.jsx';
import TimelineSection from './components/TimelineSection.jsx';
import DarshanTimeSaver from './components/DarshanTimeSaver.jsx';
import PackageDetails from './components/PackageDetails.jsx';
import StickyBookingForm from './components/StickyBookingForm.jsx';
import TestimonialsSection from './components/TestimonialsSection.jsx';
import FAQSection from './components/FAQSection.jsx';
import GuidesSection from './components/GuidesSection.jsx';
import ContactSupport from './components/ContactSupport.jsx';
import Footer from './components/Footer.jsx';
import FloatingActions from './components/FloatingActions.jsx';

const App = () => {
  return (
    <div className="bg-gray-50 text-gray-900 font-sans">
      <HeroSection />
      <TimelineSection />
      <DarshanTimeSaver />
      <PackageDetails />
      <TestimonialsSection />
      <FAQSection />
      <GuidesSection />
      <ContactSupport />
      <Footer />
      <StickyBookingForm />
      <FloatingActions />
    </div>
  );
};

export default App;
