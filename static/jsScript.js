
type = "text/javascript" >
document.addEventListener("DOMContentLoaded", function () {
    let btn = document.querySelector("#showf");
        btn.addEventListener("click", async function () {
            let eq = document.querySelector("#eq");
            let eq2 = eq.value.replace("+", "%2b");
            let to = document.querySelector("#to");
            let from = document.querySelector("#from");

            let response = await fetch( "/check?equation=" + eq2 + "&to=" + to.value + "&from=" + from.value );
            let pointsSol = await response.json();
            let points2 = pointsSol[0];
            let sol = pointsSol[1];

            console.log(sol);

            document.querySelector("ul").innerHTML = sol;

            google.charts.load("current", { packages: ["corechart"] });
            google.charts.setOnLoadCallback(drawChart);

            function drawChart() {
                var datatable = google.visualization.arrayToDataTable(points2);
                var options = {
                    title: "Your Function! 🐱‍🏍",
                    curveType: "function",
                    legend: { position: "bottom" },
                };
                var chart = new google.visualization.LineChart(
                    document.getElementById("curve_chart")
                );
                chart.draw(datatable, options);
            }
        });
});
