import './Form.css';

function generateHours() {
  const optionList = [];
  for (let i=0; i<=5; ++i) {
    let option = String(i);
    optionList.push(<option value={option}>{option}</option>);
  }
  return optionList;
}

function Form3() {
  return (
    <div className="Form">
      <h3 className="form-header basic-header-margin">
          Question 3 - How many hours do you want to spend on leisure...
      </h3>
      <div className="form-elements leisure-display">
          <div className="form-line">
            <label htmlFor="before-leisure">Before work?</label>
            <select name="before-leisure" id="before-leisure">{generateHours()}</select>
          </div>
          <div className="form-line">
            <label htmlFor="after-leisure">After work?</label>
            <select name="after-leisure" id="after-leisure">{generateHours()}</select>
          </div>
      </div>
      
    </div>
  );
}

export default Form3;
