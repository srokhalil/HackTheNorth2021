// Update master form state
const formSwitch = (stage, formState, updateMasterForm) => {
    // masterForm should be a deep copy of the state
    const masterForm = JSON.parse(JSON.stringify(formState))
    // Check which stage we are using
    switch (stage) {
        case 1:
            masterForm["hours"]["start-work"] = parseInt(document.getElementById("start-time").value);
            masterForm["hours"]["end-work"] = parseInt(document.getElementById("end-time").value);
            masterForm["hours"]["wake"] = parseInt(document.getElementById("wake-time").value);
            masterForm["hours"]["sleep"] = parseInt(document.getElementById("sleep-time").value);
            masterForm["hours"]["work-break"] = parseInt(document.getElementById("lunch-time").value);
            break;
        case 2:
            const checkboxes = document.getElementsByTagName("input");
            const day_array = [];
            Array.from(checkboxes).forEach(checkbox => {
                if (checkbox.checked) {
                    day_array.push(weekdayToNumber(checkbox.name));
                }
            })
            masterForm["hours"]["days-worked"] = day_array;
            break;
        case 3:
            masterForm["hours"]["hours-before-work"] = parseInt(document.getElementById("before-leisure").value);
            masterForm["hours"]["hours-after-work"] = parseInt(document.getElementById("after-leisure").value);
            break;
        case 4:
            masterForm["personal_information"]["name"] = document.getElementById("name").value;
            masterForm["personal_information"]["post-code"] = document.getElementById("postal-code").value;
            masterForm["personal_information"]["birthday"] = document.getElementById("birthday").value;
            masterForm["personal_information"]["email"] = document.getElementById("email").value;
            masterForm["personal_information"]["city"] = document.getElementById("city").value;
            masterForm["personal_information"]["province"] = document.getElementById("province").value;
            masterForm["personal_information"]["country"] = document.getElementById("country").value;
            break;
        case 5:
            const category_checkboxes = document.getElementsByTagName("input");
            const category_array = [];
            Array.from(category_checkboxes).forEach(checkbox => {
                if (checkbox.checked) {
                    category_array.push(checkbox.id);
                }
            })
            masterForm["activities"] = category_array;
            break;
        default:
            break;
    }
    updateMasterForm(masterForm)
}

// Convert string of weekday to number (0-6, 0 is Sunday)
const weekdayToNumber = (day) => {
    switch (day) {
        case "Sunday":
            day = 0;
            break;
        case "Monday":
            day = 1;
            break;
        case "Tuesday":
            day = 2;
            break;
        case "Wednesday":
            day = 3;
            break;
        case "Thursday":
            day = 4;
            break;
        case "Friday":
            day = 5;
            break;
        case "Saturday":
            day = 6;
            break;
        default:
            break;
    }
    return day;
}

export default formSwitch;