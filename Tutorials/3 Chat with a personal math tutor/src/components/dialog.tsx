import React from "react";
import Button from "@mui/material/Button";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import DialogTitle from "@mui/material/DialogTitle";
import Dialog from "@mui/material/Dialog";
import LoadingButton from "@mui/lab/LoadingButton";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";

export interface DialogProps {
  open: boolean;
  onClose: () => void;
}

function SimpleDialog(props: DialogProps) {
  const { open: dialogOpen, onClose } = props;

  const [loadingAssistants, setLoadingAssistants] = React.useState(false);
  const [loadingThreads, setLoadingThreads] = React.useState(false);

  const [extractedInfo, setExtractedInfo] = React.useState([]);

  const handleClose = () => {
    setLoadingAssistants(false);
    setLoadingThreads(false);
    onClose();
  };

  const getAllAssistants = async (e: any) => {
    setLoadingAssistants(true);
    e.preventDefault();

    console.log("znotraj funkcije 1: ", loadingAssistants);

    setLoadingAssistants(true);

    console.log("znotraj funkcije 2: ", loadingAssistants);

    try {
      console.log("znotraj try: ", loadingAssistants);

      const response = await fetch(`/api/listAssistants`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        const getResponse = await response.json();
        const getData = getResponse.message.body.data;

        const extractedInfo = getData.map((assistant: any) => {
          return {
            id: assistant.id,
            name: assistant.name,
            instructions: assistant.instructions,
          };
        });

        setTimeout(() => {
          setExtractedInfo(extractedInfo);
          console.log(extractedInfo);
          console.log("konec timeouta: ", loadingAssistants);
        }, 2000);
      } else {
        console.error(response);
      }
    } catch (error: any) {
      console.error(error);
    } finally {
      setLoadingAssistants(false);
    }
  };

  const getAllThreads = async (e: any) => {
    e.preventDefault();

    setLoadingThreads(true);

    try {
      // ... (code for fetching threads)
    } catch (error: any) {
      console.error(error);
    } finally {
      setLoadingThreads(false);
    }
  };

  return (
    <Dialog
      onClose={handleClose}
      open={dialogOpen}
      sx={{
        ".MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiDialog-paper": {
          backgroundColor: "rgb(249 250 251)",
          borderRadius: "0.5rem",
          padding: "1rem",
        },
      }}
      fullWidth
      maxWidth="sm"
    >
      <DialogTitle className="font-medium px-4">
        Get values for env variables
      </DialogTitle>
      <List sx={{ pt: 0 }}>
        <ListItem>
          <LoadingButton
            onClick={getAllAssistants}
            loading={loadingAssistants}
            variant="contained"
            className="text-white bg-gray-800 hover:bg-gray-600 w-full"
            sx={{
              "&.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary":
                {
                  color: "white",
                  backgroundColor: "rgba(52,53,65,1)",
                  borderColor: "rgba(255, 255, 255, 0.5)",
                  borderRadius: "0.5rem",
                },
            }}
          >
            List all assistants
          </LoadingButton>
        </ListItem>
        {extractedInfo.length > 0 && (
          <ListItem>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>ID</TableCell>
                  <TableCell>Name</TableCell>
                  <TableCell>Instructions</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {extractedInfo.map((assistant: any) => (
                  <TableRow key={assistant.id}>
                    <TableCell>{assistant.id}</TableCell>
                    <TableCell>{assistant.name}</TableCell>
                    <TableCell>{assistant.instructions}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </ListItem>
        )}
        <ListItem onClick={getAllThreads}>
          <LoadingButton
            loading={loadingThreads}
            variant="contained"
            className="text-white bg-gray-800 hover:bg-gray-600 w-full"
            sx={{
              "&.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary":
                {
                  color: "white",
                  backgroundColor: "rgba(52,53,65,1)",
                  borderColor: "rgba(255, 255, 255, 0.5)",
                  borderRadius: "0.5rem",
                },
            }}
          >
            List all threads
          </LoadingButton>
        </ListItem>
      </List>
    </Dialog>
  );
}

export default function SimpleDialogDemo() {
  const [open, setOpen] = React.useState(false);

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button
        variant="contained"
        onClick={handleOpen}
        sx={{
          "&.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary":
            {
              color: "rgba(0, 0, 0, 0.8)",
              fontWeight: "600",
              backgroundColor: "rgba(255, 255, 255, 1)",
              borderColor: "rgba(255, 255, 255, 0.5)",
              borderRadius: "0.5rem",
            },
          "&.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary:hover":
            {
              backgroundColor: "rgba(255, 255, 255, 0.8)",
            },
        }}
      >
        Get values for env variables
      </Button>
      <SimpleDialog open={open} onClose={handleClose} />
    </div>
  );
}
