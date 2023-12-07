import React from "react";
import copy from "clipboard-copy";
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
import Snackbar from "@mui/material/Snackbar";
import MuiAlert, { AlertProps, AlertColor } from "@mui/material/Alert";
import { RxClipboardCopy } from "react-icons/rx";

export interface DialogProps {
  open: boolean;
  onClose: () => void;
}

// Define the Alert component using MuiAlert
const Alert = React.forwardRef<HTMLDivElement, AlertProps>(function Alert(
  props,
  ref
) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

// Define the GetValuesForEnvVariablesDialog component
function GetValuesForEnvVariablesDialog(props: DialogProps) {
  // Destructure props
  const { open: dialogOpen, onClose } = props;

  // State variables for loading states, snackbar, and extracted information
  const [loadingAssistants, setLoadingAssistants] = React.useState(false);
  const [loadingThread, setLoadingThread] = React.useState(false);
  const [snackbarOpen, setSnackbarOpen] = React.useState(false);
  const [snackbarSeverity, setSnackbarSeverity] = React.useState("");
  const [snackbarMessage, setSnackbarMessage] = React.useState("");
  const [extractedInfoForAssistants, setExtractedInfoForAssistants] =
    React.useState([]);
  const [extractedInfoForThread, setExtractedInfoForThread] = React.useState<
    { id: any; created_at: any }[]
  >([]);

  // Function to close the dialog
  const handleDialogClose = () => {
    setLoadingAssistants(false);
    setLoadingThread(false);
    onClose();
  };

  // Function to fetch and list all assistants
  const assistantsFunction = async (e: any) => {
    e.preventDefault();
    setLoadingAssistants(true);

    try {
      const response = await fetch(`/api/listAssistants`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        const getResponse = await response.json();
        const getData = getResponse.message.body.data;

        const extractedInfoForAssistants = getData.map((assistant: any) => {
          return {
            id: assistant.id,
            name: assistant.name,
            instructions: assistant.instructions,
          };
        });

        setExtractedInfoForAssistants(extractedInfoForAssistants);
      } else {
        console.error(response);
      }
    } catch (error: any) {
      console.error(error);
    } finally {
      setLoadingAssistants(false);
    }
  };

  // Function to create a new thread
  const threadFunction = async (e: any) => {
    e.preventDefault();
    setLoadingThread(true);

    try {
      const response = await fetch(`api/createThread`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        const getResponse = await response.json();
        const getData = getResponse.message;

        const threadId = getData.id;
        const threadCreatedAt = getData.created_at;

        setExtractedInfoForThread([
          {
            id: threadId,
            created_at: threadCreatedAt,
          },
        ]);
      } else {
        console.error(response);
      }
    } catch (error: any) {
      console.error(error);
    } finally {
      setLoadingThread(false);
    }
  };

  // Function to format Unix timestamp to a readable date
  const formatUnixTimestamp = (
    timestamp: number,
    locale: string,
    timeZone: string
  ) => {
    const milliseconds = timestamp * 1000;
    return new Intl.DateTimeFormat(locale, {
      year: "numeric",
      month: "numeric",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      timeZone: timeZone,
    }).format(new Date(milliseconds));
  };

  // Function to copy text to clipboard
  const copyToClipboard = async (text: string, idType: string) => {
    try {
      await copy(text);
      setSnackbarOpen(true);
      setSnackbarSeverity("success");
      setSnackbarMessage(`${idType} ID copied to clipboard`);
    } catch (error) {
      console.error("Error copying to clipboard:", error);
      setSnackbarOpen(true);
      setSnackbarSeverity("error");
      setSnackbarMessage(`Error copying ${idType} ID to clipboard`);
    }
  };

  // Function to handle Snackbar close event
  const handleSnackbarClose = (
    event: React.SyntheticEvent | Event,
    reason?: string
  ) => {
    if (reason === "clickaway") {
      return;
    }
    setSnackbarOpen(false);
  };

  // Function to map severity to Alert color
  const mapSeverityToAlertColor = (severity: string): AlertColor => {
    switch (severity) {
      case "success":
        return "success";
      case "error":
        return "error";
      case "warning":
        return "warning";
      case "info":
        return "info";
      default:
        return "info";
    }
  };

  // Return the JSX structure for the component
  return (
    <>
      <Dialog
        onClose={handleDialogClose}
        open={dialogOpen}
        sx={{
          ".MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiDialog-paper":
            {
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
          {/* Button to list all assistants */}
          <ListItem>
            <LoadingButton
              onClick={assistantsFunction}
              loading={loadingAssistants}
              variant="outlined"
              className="w-full"
            >
              List all assistants
            </LoadingButton>
          </ListItem>
          {/* Table to display extracted information for assistants */}
          {extractedInfoForAssistants.length > 0 && (
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
                  {extractedInfoForAssistants.map((assistant: any) => (
                    <TableRow key={assistant.id}>
                      <TableCell className="whitespace-nowrap">
                        {assistant.id}
                        {/* ClipboardCopy icon to copy ID to clipboard */}
                        <RxClipboardCopy
                          className="inline ml-3 hover:cursor-pointer"
                          onClick={() =>
                            copyToClipboard(assistant.id, "Assistant")
                          }
                        />
                      </TableCell>
                      <TableCell>{assistant.name}</TableCell>
                      <TableCell>{assistant.instructions}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </ListItem>
          )}
          {/* Button to create a new thread */}
          <ListItem>
            <LoadingButton
              onClick={threadFunction}
              loading={loadingThread}
              variant="outlined"
              className="w-full"
            >
              Create a new Thread
            </LoadingButton>
          </ListItem>
          {/* Table to display extracted information for the thread */}
          {extractedInfoForThread.length > 0 && (
            <ListItem>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell>ID</TableCell>
                    <TableCell>Created at</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {extractedInfoForThread.map((thread: any) => (
                    <TableRow key={thread.id}>
                      <TableCell className="whitespace-nowrap">
                        {thread.id}
                        {/* ClipboardCopy icon to copy ID to clipboard */}
                        <RxClipboardCopy
                          className="inline ml-3 hover:cursor-pointer"
                          onClick={() => copyToClipboard(thread.id, "Thread")}
                        />
                      </TableCell>
                      <TableCell>
                        {formatUnixTimestamp(
                          thread.created_at,
                          "si-SL",
                          "Europe/Ljubljana"
                        )}
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </ListItem>
          )}
        </List>
      </Dialog>
      {/* Snackbar for displaying copy success/error messages */}
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={5000}
        onClose={handleSnackbarClose}
        anchorOrigin={{ vertical: "bottom", horizontal: "center" }}
      >
        {/* Alert component for Snackbar messages */}
        <Alert
          onClose={handleSnackbarClose}
          severity={mapSeverityToAlertColor(snackbarSeverity)}
        >
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </>
  );
}

// Define the HandleDialogOpening component
export default function HandleDialogOpening() {
  // State variable for dialog open/close
  const [open, setOpen] = React.useState(false);

  // Function to open the dialog
  const handleDialogOpen = () => {
    setOpen(true);
  };

  // Function to close the dialog
  const handleDialogClose = () => {
    setOpen(false);
  };

  // Return the JSX structure for the component
  return (
    <div>
      {/* Button to open the dialog */}
      <Button
        variant="outlined"
        onClick={handleDialogOpen}
        sx={{
          "&.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.MuiButton-outlinedPrimary":
            {
              color: "rgba(0, 0, 0, 0.8)",
              fontWeight: "600",
              backgroundColor: "rgba(255, 255, 255, 1)",
              borderColor: "rgba(255, 255, 255, 0.5)",
              borderRadius: "0.5rem",
            },
          "&.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.MuiButton-outlinedPrimary:hover":
            {
              backgroundColor: "rgba(255, 255, 255, 0.8)",
            },
        }}
      >
        Get values for env variables
      </Button>
      {/* Render GetValuesForEnvVariablesDialog component */}
      <GetValuesForEnvVariablesDialog open={open} onClose={handleDialogClose} />
    </div>
  );
}
