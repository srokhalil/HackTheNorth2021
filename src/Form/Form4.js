import './Form.css';

function Form4() {
  return (
    <div className="Form">
      <h3 className="form-header basic-header-margin">
          Question 4 - Could you tell us a little bit about yourself?
      </h3>
      <div className="form-elements text-elements">
          <div className="form-line text-line">
            <label htmlFor="name">Name:</label>
            <input name="name" id="name"></input>
          </div>
          <div className="form-line text-line">
            <label htmlFor="city">City:</label>
            <input name="city" id="city"></input>
          </div>
          <div className="form-line text-line">
            <label htmlFor="email">Email:</label>
            <input name="email" id="email"></input>
          </div>
          <div className="form-line text-line">
            <label htmlFor="province">Province:</label>
            <input name="province" id="province"></input>
          </div>
          <div className="form-line text-line">
            <label htmlFor="birthday">Birthday:</label>
            <input name="birthday" id="birthday" placeholder="YYYY-MM-DD"></input>
          </div>
          <div className="form-line text-line">
            <label htmlFor="country">Country:</label>
            <input name="country" id="country"></input>
          </div>
          <div className="form-line text-line">
            <label htmlFor="postal-code">Postal code:</label>
            <input name="postal-code" id="postal-code"></input>
          </div>
      </div>
      
    </div>
  );
}

export default Form4;