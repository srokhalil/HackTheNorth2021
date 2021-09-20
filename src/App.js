import './App.css';
import formSwitch from './formSwitching.js';
import { useEffect, useState } from 'react';

import Start from './Form/Start.js';
import Calendar from './Form/Calendar';
import Form1 from './Form/Form1.js';
import Form2 from './Form/Form2.js';
import Form3 from './Form/Form3.js';
import Form4 from './Form/Form4.js';
import Form5 from './Form/Form5.js';

import start_gradient from './assets/start_gradient.svg';
import question_gradient from './assets/question_gradient.svg';
import room from './assets/room.svg';
import room2 from './assets/room2.svg';

const MAX_STEP = 6;

function App() {
  // Image preloading
  useEffect(() => {
    const imageList = [start_gradient, question_gradient, room, room2]
    imageList.forEach((image) => {
      new Image().src = image
    });
  }, [])

  // Master form state
  const [formState, setFormState] = useState({
    "personal_information": {
        "name": "test",
        "post-code": "code",
        "birthday": "yyyy-mm-dd"
    },
    "hours": {
        "start-work": 9,
        "end-work": 17,
        "wake": 7,
        "sleep": 23,
        "work-break-time": 12,
        "work-break": 1,
        "hours-before-work": 1,
        "hours-after-work": 3
    },
    "activities": ["sports", "entertainment", "creative", "others"]
  })
  // Current step state
  const [currentStep, setCurrentStep] = useState(0)

  // Render start screen if we haven't started yet
  if (currentStep === 0) {
    return (
    <div className="App start-gradient">
      <Start/>
      <button className="start-button" onClick={()=>setCurrentStep(1)}>
        Start
      </button>
    </div>
    );
  }
  // Chose which step to render
  let formElement;
  let image;
  switch (currentStep) {
    case 1:
      formElement = <Form1/>;
      image = <img src={room} alt="room" className="image"/>
      break;
    case 2:
      formElement = <Form2 />;
      image = <img src={room2} alt="room2" className="image"/>
      break;
    case 3:
        formElement = <Form3 />;
        break;
    case 4:
        formElement = <Form4 />;
        break;
    case 5:
        formElement = <Form5 />;
        break;
    case MAX_STEP:
      return (
        <div className="App question-gradient">
          <Calendar masterFormState={formState}/>
        </div>
      )
    default:
      break;
  }
  // See if we can render the next button
  let nextButton;
  if (currentStep !== MAX_STEP) {
    nextButton = 
    <button className="next" 
    onClick={()=>{formSwitch(currentStep, formState, setFormState);setCurrentStep(currentStep+1)}}>
      { currentStep === MAX_STEP - 1 ? "Finish" : "Next" }
    </button>
  } else {
    nextButton = 
    <button disabled={true} className="next">
      Next
    </button>
  }
  // See if we can render the back button
  let backButton;
  if (currentStep > 0) {
    backButton = 
    <button className="back" onClick={()=>setCurrentStep(currentStep-1)}>
      Back
    </button>
  } else {
    backButton = 
    <button disabled={true} className="back">
      Back
    </button>
  }
  return (
    <div className="App question-gradient">
      {image ? 
      <div className="wrapper">
        {formElement}
        {image}
      </div> : formElement}
      <div className="button-box">
        {backButton}
        {nextButton}
      </div>
    </div>
  );
}

export default App;
