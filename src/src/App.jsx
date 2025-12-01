import React from 'react';
import HeroSection from './components/HeroSection.jsx';
import TimelineSection from './components/TimelineSection.jsx';
import DarshanTimeSaver from './components/DarshanTimeSaver.jsx';
import PackageDetails from './components/PackageDetails.jsx';

export default function App() {
  return (
    <>
      <HeroSection />
      <TimelineSection />
      <DarshanTimeSaver />
      <PackageDetails />
    </>
  );
}
