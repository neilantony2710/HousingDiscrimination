import Container from "@mui/material/Container";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import IncomeGraph from "./IncomeGraph";
import DTIGraph from "./DTIGraph";
import RawGraph from "./RawGraph";
import CssBaseline from "@mui/material/CssBaseline";
import Grid from "@mui/material/Unstable_Grid2";
import Card from "@mui/material/Card";
import Link from "@mui/material/Link";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
});

export default function Board() {
  return (
    <>
      <ThemeProvider theme={darkTheme}>
        <CssBaseline />
        <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
          <Grid container spacing={3}>
            <Grid xs={6}>
              <Card>
                <CardContent>
                  <Typography variant="h4"> Introduction </Typography>
                  <Typography variant="b1"> This website visualizes the surprising amount of housing discrimination that still exists in the United States. The three graphs display the rates at which black and white people get their housing loans denied. The first graph shows the overall denial percentages. The second graph controls the data for income. The third graph controls the data for debt to income ratio. In all three graphs a concerning pattern emerges: Black Americans have disproportionately higher rates of denied loans.                  </Typography>
                  <Typography variant="b1"> *Note: all data values truncated to two decimal points </Typography>
                </CardContent>
              </Card>
            </Grid>
            <Grid xs={6}>
              <Card>
                <CardContent>
                  <Typography variant="h4"> Sources / Collaborators </Typography>
                  <Typography variant="h6"> Mentors: </Typography>
                  <Typography variant="body1">Aspriring Scholars Directed Research Program & Dr. Phil Mui </Typography>
                  <Typography variant="h6"> Peer Researchers: </Typography>
                  <Typography variant="body1">Neil Antony, Nicholas Chang, Aditi Ghosh </Typography>
                  <Typography variant="h6"> Sources: </Typography>
                  <Link href="https://ffiec.cfpb.gov/data-publication/snapshot-national-loan-level-dataset/2022">Data Source</Link>
                  <Typography variant="h6"></Typography>
                  <Link href="https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/public-lar-schema"> LAR Scheme of Source (Structure of csv data file)</Link>

                </CardContent>
              </Card>
            </Grid>
            <Grid xs={12}>
              <Card>
                <CardContent>
                  <Typography variant="h5" textAlign ="center"> Raw Data </Typography>
                  <RawGraph />
                </CardContent>
              </Card>
            </Grid>
            <Grid xs={12}>
              <Card>
                <CardContent>
                  <Typography variant="h5" textAlign ="center"> Controlled for Income </Typography>
                  <IncomeGraph />
                </CardContent>
              </Card>
            </Grid>
            <Grid xs={12}>
              <Card>
                <CardContent>
                  <Typography variant="h5" textAlign ="center"> Controlled for Debt to Income Ratio  </Typography>
                  <DTIGraph />
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </Container>
      </ThemeProvider>
    </>
  );
}
