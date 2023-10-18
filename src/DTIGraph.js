import { BarChart } from "@mui/x-charts/BarChart";

export default function DTIGraph() {
  return (
    <>
      <BarChart
      width = {500}
      height = {400}
        xAxis={[
          {
            label: "Debt-to-Income Ratio Groups",
            scaleType: "band",
            data: ["<20", "20-30", "30-40", "40-50", "50-60", ">60"],
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
            data: [20.19,12.14,11.36,12.74,12.14,87.7],
            color: "#FEFBEA",
          },
          {
            label: "Black",
            data:  [48.12,27.17,21.31,20.66,27.17,90.55],
            color: "#A792B3",
          },
        ]}
        s
      />
    </>
  );
}
