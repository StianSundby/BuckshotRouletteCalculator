function updateCheckboxes(index, type) {
	var live = document.getElementById("live" + index);
	var blank = document.getElementById("blank" + index);
	console.log(index);
	if (type === "live" && live.checked) {
		blank.checked = false;
	} else if (type === "blank" && blank.checked) {
		live.checked = false;
	}
}
