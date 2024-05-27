type =
    "text/javascript" >
    document.addEventListener("DOMContentLoaded", function () {
        let btn = document.querySelector(".srchBtn");
        console.log(btn);
        btn.addEventListener("click", async function () {
            console.log("hello boys");
            let eq = document.querySelector("#eq");
            let eq2 = eq.value.replaceAll("+", "%2b");
            let to = document.querySelector("#to");
            let from = document.querySelector("#from");
            console.log("/check?equation=" , eq2 , "&to=" , to.value , "&from=" , from.value);

            let response = await fetch(
                "/check?equation=" +
                    eq2 +
                    "&to=" +
                    to.value +
                    "&from=" +
                    from.value
            );
            let pointsSol = await response.json();
            let points2 = pointsSol[0];
            let sol = pointsSol[1];

            console.log(sol);

            document.querySelector("#eq_slot").innerHTML = sol;

            google.charts.load("current", { packages: ["corechart"] });
            google.charts.setOnLoadCallback(drawChart);

            function drawChart() {
                var datatable = google.visualization.arrayToDataTable(points2);
                var options = {
                    title: "Your Function! 🐱‍🏍",
                    curveType: "function",
                    legend: { position: "bottom" },
                    backgroundColor: 'transparent',
                    'chartArea': { 'width': '90%', 'height': '80%' },
                    lineWidth: 2,
                    colors: ["#9b679c"],

                };  
                var chart = new google.visualization.LineChart(
                    document.getElementById("curve_chart")
                );
                chart.draw(datatable, options);
            }
        });
        let popup = document.querySelector("#popbutton");
        popup.addEventListener("select", async function () {
            console.log('ok where is the pop')
        })
    });
    function popup() {
        console.log('ok cat')
        var popup = document.getElementById("myPopup");
        popup.classList.toggle("show");
};
function clearit() {
    // if there is a to or from, delete them first, then delete the equation next
    to = document.getElementById('to');
    from = document.getElementById('from');
    if (to.value == "" && from.value=="" ){
        document.getElementById('eq').value = "";
    } else {
        document.getElementById('to').value = "";
        document.getElementById('from').value = "";
    }
    
};
document.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.querySelector(".srchBtn").click();
    }
});
