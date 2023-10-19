import { BarChart } from "@mui/x-charts/BarChart";

export default function IncomeGraph() {
  return (
    <>
      <BarChart
      width = {1100}
      height = {400}
        xAxis={[
          {
            label: "Income (in thousands of USD)",
            scaleType: "band",
            data: ["<10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90", "90-100", ">100"],
          },
        ]}
        yAxis={
            [
                {label: "Percent of Applicants Denied"}
            ]
        }
        
        series={[
          {
            label: "White",
            data: [
              46.3, 49.1, 35.13, 26.51, 21.24, 17.95, 16.47, 15.33, 14.06,
              13.35, 10.99,
            ],
            color: "#FEFBEA",
          },
          {
            label: "Black",
            data: [
              54.48, 60.86, 47.96, 38.18, 31.46, 26.83, 24.73, 22.97, 21.67,
              20.63, 18.8,
            ],
            color: "#A792B3",
          },
        ]}
        s
      />
    </>
  );
}
