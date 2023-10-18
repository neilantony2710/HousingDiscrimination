import Container from "@mui/material/Container";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import IncomeGraph from "./IncomeGraph";
import DTIGraph from "./DTIGraph";
import RawGraph from "./RawGraph";
import CssBaseline from "@mui/material/CssBaseline";
import Grid from "@mui/material/Unstable_Grid2";
import Card from "@mui/material/Card";
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
                  <RawGraph />
                </CardContent>
              </Card>
            </Grid>
            <Grid xs={6}>
              <Card>
                <CardContent>
                  <Typography variant="h5"> Raw Data Graph</Typography>
                </CardContent>
              </Card>
            </Grid>
            <Grid xs={6}>
              <Card>
                <CardContent>
                  <IncomeGraph />
                </CardContent>
              </Card>
            </Grid>
            <Grid xs={6}>
              <Card>
                <CardContent>
                  <Typography variant="h5">Normalized for Income</Typography>
                </CardContent>
              </Card>
            </Grid>
            <Grid xs={6}>
              <Card>
                <CardContent>
                  <DTIGraph />
                </CardContent>
              </Card>
            </Grid>
            <Grid xs={6}>
              <Card>
                <CardContent>
                  <Typography variant="h5">Normalized for Debt to Income ratio</Typography>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </Container>
      </ThemeProvider>
    </>
  );
}
