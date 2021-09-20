import './Form.css';
import { Buffer } from 'buffer';

function Calendar(props) {
  const download = async () => {
    const requestBodyObject = props.masterFormState;
    console.log(requestBodyObject);
    // TODO: Call function that sends the request, and returns the csv string
    const response = await fetch("/csv", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBodyObject)
    });
    let csvContent = "";
    let reader = response.body.getReader();
    reader.read().then(
      function processText({ done, value }) {
      if (done) {
        return;
      }
      // value for fetch streams is a Uint8Array
      const chunk = Buffer.from(value);
      const bstring = chunk.toString('utf8');
      csvContent += bstring;
      return reader.read().then(processText);
    }).then(() => {
      csvContent = "data:text/csv;charset=utf-8," + csvContent;
      let encodedUri = encodeURI(csvContent);
      let link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "my_schedule.csv");
      document.body.appendChild(link); // Required for FF
      link.click(); // This will download the data file named "my_schedule.csv".
      document.body.removeChild(link);
    });
  }
  return (
    <div className="Calendar">
        <div className="horizontal-line">
            <h3 className="calendar-header">
                Download your schedule for next week!
            </h3>
            <button className="download-button" onClick={download}>
                Download
            </button>
        </div>
    </div>
  );
}

export default Calendar;