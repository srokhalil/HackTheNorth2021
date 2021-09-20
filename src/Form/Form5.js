import './Form.css';

function Form5() {
  return (
    <div className="Form">
      <h3 className="form-header basic-header-margin">
          Question 5 - Which type of activity would you like to do in your free time?
      </h3>
      <div className="check-elements activities">
          <div className="check-line">
            <input type="checkbox" id="creativity" name="creativity"></input>
            <label htmlFor="creativity">Creativity</label>
          </div>
          <div className="check-line">
            <input type="checkbox" id="entertainment" name="entertainment"></input>
            <label htmlFor="entertainment">Entertainment</label>
          </div>
          <div className="check-line">
            <input type="checkbox" id="sports" name="sports"></input>
            <label htmlFor="sports">Sports</label>
          </div>
          <div className="check-line">
            <input type="checkbox" id="others" name="others"></input>
            <label htmlFor="others">Other</label>
          </div>
      </div>
    </div>
  );
}

export default Form5;