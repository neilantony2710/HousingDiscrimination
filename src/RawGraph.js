import { BarChart } from "@mui/x-charts/BarChart";

export default function RawGraph() {
  return (
    <>
      <BarChart
        width={500}
        height={400}
        yAxis={[{ label: "Percent of Applicants Denied" }]}
        xAxis={[
          {
            label: "Income Groups (in thousands of USD)",
            scaleType: "band",
            data: ["", ""],
          },
        ]}
        series={[
          {
            label: "White",
            data: [15.44],
            color: "#FEFBEA",
          },
          {
            label: "Black",
            data: [25.18],
            color: "#A792B3",
          },
        ]}
        s
      />
    </>
  );
}
