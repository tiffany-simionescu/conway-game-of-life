import { makeStyles } from "@material-ui/core/styles";

export const menuStyles = makeStyles(theme => ({
  root: {
    // height: "100vh",
    // // float: "right",
    // position: "absolute",
    // right: "0"
    // backgroundColor: "black"
    // top: "-500px"

  },
  // aboutMenu: {
  //   display: "flex",
  //   flexDirection: "column",
  //   alignItems: "center",
  //   float: "left",
  //   width: "150px",
  //   height: "100vh",
  //   backgroundColor: "grey",
  //   position: "fixed",
  //   marginTop: "-1%",
  //   paddingTop: "20px",
  //   marginLeft: "-8px"
  // },
  ruleMenu: {
    marginTop: "-1%",
    width: "250px",
    // height: "100vh",
    backgroundColor: "lightgrey",
    position: "fixed",
    left: "84%"
  },
  accordionType: {
    // height: "60vh"
  },
  // heading: {
  //   fontSize: theme.typography.pxToRem(15),
  //   fontWeight: theme.typography.fontWeightRegular,
  // },
  // icon: {
  //   background: theme.palette.primary.main,
  //   width: "80px",
  //   height: "80px",
  //   borderRadius: "20px",
  //   margin: "20px 0"
  // },
  aboutMenu: {
    // marginTop: "-1%",
    // height: "100vh",
    // width: "350px",
    // height: "auto",
    // backgroundColor: "lightgrey",
    // // float: "right",
    // // position: "fixed",
    // // float: "left"
    // // position: "absolute",
    // right: "0"
    // marginTop: "-1%",
    width: "350px",
    // height: "100vh",
    // backgroundColor: "lightgrey",
    // backgroundColor: "black",
    position: "relative",
    left: "25%",
    marginTop: "-25%"
  },
  innerMenu: {
    // background: linear-gradient(#062474, #000);
    // color: #039595;
    // padding: 10px;
    // margin-top: 10px;
    // border-radius: 10px;
    // box-shadow: 5px 10px 18px darkslategray;
    backgroundColor: "black",
    // background: "linear-gradient(#062474, #000)",
    background: "linear-gradient(#000, #062474)",
    color: "#90cccc",
    padding: "10px",
    // marginTop: "10px",
    // borderRadius: "10px",
    boxShadow: "5px 10px 18px darkslategray" 
  }
}));
