import { BarChart } from "@mui/x-charts/BarChart";

export default function RawGraph() {
  return (
    <>
      <BarChart
        width={1100}
        height={400}
        yAxis={[{ label: "Percent of Applicants Denied" }]}
        xAxis={[
          {
            label: "",
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
