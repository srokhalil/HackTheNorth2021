import './Form.css';

function timeDropdowns() {
  const optionList = [];
  for (let i=0; i<24; ++i) {
    let option = String(i).padStart(2, '0') + ":00";
    optionList.push(<option value={i}>{option}</option>);
  }
  return optionList;
}

function Form1() {
  return (
    <div className="Form">
      <h3 className="form-header basic-header-margin">
          Question 1 - What time do you...
      </h3>
      <div className="form-elements">
          <div className="form-line">
            <label htmlFor="wake-time">Wake up?</label>
            <select name="wake-time" id="wake-time">{timeDropdowns()}</select>
          </div>
          <div className="form-line">
            <label htmlFor="end-time">End work?</label>
            <select name="end-time" id="end-time">{timeDropdowns()}</select>
          </div>
          <div className="form-line">
            <label htmlFor="start-time">Start work?</label>
            <select name="start-time" id="start-time">{timeDropdowns()}</select>
          </div>
          <div className="form-line">
            <label htmlFor="sleep-time">Go sleep?</label>
            <select name="sleep-time" id="sleep-time">{timeDropdowns()}</select>
          </div>
          <div className="form-line">
            <label htmlFor="lunch-time">Eat lunch?</label>
            <select name="lunch-time" id="lunch-time">{timeDropdowns()}</select>
          </div>
      </div>
    </div>
  );
}

export default Form1;