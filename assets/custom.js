document.addEventListener('keyup', e => {

    console.log("addEventListener - keyup - start")


    let pid = e.target.id;

    console.log(pid)

    if (pid === "search") {

        console.log("search start");

        var input, filter, table, tr, td, i, txtValue, col;
        input = document.getElementById("search");
        filter = input.value;
        table = document.getElementById("table-body");
        tr = table.getElementsByTagName("tr");

        // Loop through all table rows, and hide those who don't match the search query
        for (i = 0; i < tr.length; i++) {
            for (col = 0; col < 5; col++) {
                td = tr[i].getElementsByTagName("td")[col];
                if (td) {
                    txtValue = td.textContent || td.innerText;
                    if (txtValue.indexOf(filter) > -1) {
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