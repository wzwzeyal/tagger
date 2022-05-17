document.addEventListener('keyup', e => {

    console.log("addEventListener - keyup - start")


    let pid = e.target.id;

    console.log(pid)

    if (pid === "search") {

        console.log("search start");

        var input, filter, table, tr, td, i, txtValue, col;
        input = document.getElementById("search");
        filter = input.value.toUpperCase();
        table = document.getElementById("table-body");
        tr = table.getElementsByTagName("tr");

        var nof_cols = document.getElementById('table-head').rows[0].cells.length
        nof_cols = nof_cols - 1; // ignore Annotate

        // Loop through all table rows, and hide those who don't match the search query
        for (i = 0; i < tr.length; i++) {
            for (col = 0; col < nof_cols; col++) {
                td = tr[i].getElementsByTagName("td")[col];
                if (td) {
                    txtValue = td.textContent || td.innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        //find index of word 'in'
                        const index = txtValue.indexOf(filter);

                        //opening and closing tags
                        const openingTag = '<span style="background-color:yellow">'
                        const closingTag = '</span>'

                        const newHTML
                          = txtValue.slice(0, index)
                          + openingTag + filter + closingTag
                          + txtValue.slice(index + filter.length);

                        // td.innerHTML = newHTML;
                        tr[i].style.display = "";
                        break;
                    } else {
                        tr[i].style.display = "none";
                    }
                }
            }
        }
    }
    console.log("addEventListener - keyup - stop")


});

$(function() {
	const rowsPerPage = 13;
	const rows = $('#dataset-table tbody tr');
	const rowsCount = rows.length;
	const pageCount = Math.ceil(rowsCount / rowsPerPage); // avoid decimals
	const numbers = $('#numbers');

	// Generate the pagination.
	for (var i = 0; i < pageCount; i++) {
		numbers.append('<li><a href="#">' + (i+1) + '</a></li>');
	}

	// Mark the first page link as active.
	$('#numbers li:first-child a').addClass('active');

	// Display the first set of rows.
	displayRows(1);

	// On pagination click.
	$('#numbers li a').click(function(e) {
		var $this = $(this);

		e.preventDefault();

		// Remove the active class from the links.
		$('#numbers li a').removeClass('active');

		// Add the active class to the current link.
		$this.addClass('active');

		// Show the rows corresponding to the clicked page ID.
		displayRows($this.text());
	});

	// Function that displays rows for a specific page.
	function displayRows(index) {
		var start = (index - 1) * rowsPerPage;
		var end = start + rowsPerPage;

		// Hide all rows.
		rows.hide();

		// Show the proper rows for this page.
		rows.slice(start, end).show();
	}
});