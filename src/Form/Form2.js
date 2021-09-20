import './Form.css';

function Form2() {
  return (
    <div className="Form">
      <h3 className="form-header basic-header-margin">
          Question 2 - Which days do you work?
      </h3>
      <div className="check-elements">
          <div className="check-line">
            <input type="checkbox" id="sunday" name="Sunday"></input>
            <label htmlFor="sunday">Sunday</label>
          </div>
          <div className="check-line">
            <input type="checkbox" id="thursday" name="Thursday"></input>
            <label htmlFor="thursday">Thursday</label>
          </div>
          <div className="check-line">
            <input type="checkbox" id="monday" name="Monday"></input>
            <label htmlFor="monday">Monday</label>
          </div>
          <div className="check-line">
            <input type="checkbox" id="friday" name="Friday"></input>
            <label htmlFor="friday">Friday</label>
          </div>
          <div className="check-line">
            <input type="checkbox" id="tuesday" name="Tuesday"></input>
            <label htmlFor="tuesday">Tuesday</label>
          </div>
          <div className="check-line">
            <input type="checkbox" id="saturday" name="Saturday"></input>
            <label htmlFor="saturday">Saturday</label>
          </div>
          <div className="check-line">
            <input type="checkbox" id="wednesday" name="Wednesday"></input>
            <label htmlFor="wednesday">Wednesday</label>
          </div>
      </div>
    </div>
  );
}

export default Form2;