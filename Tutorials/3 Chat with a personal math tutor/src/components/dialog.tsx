import React from "react";
import Button from "@mui/material/Button";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import DialogTitle from "@mui/material/DialogTitle";
import Dialog from "@mui/material/Dialog";

const envVariables = [
  "Get value for env variable 1",
  "Get value for env variable 2",
  "Get value for env variable 3",
];

export interface SimpleDialogProps {
  open: boolean;
  onClose: (value: string) => void;
}

function SimpleDialog(props: SimpleDialogProps) {
  const { open: dialogOpen, onClose } = props;

  const [localOpen, setLocalOpen] = React.useState(false);

  const handleClose = () => {
    setLocalOpen(false);
    onClose("some value");
  };

  return (
    <Dialog
      onClose={handleClose}
      open={dialogOpen}
      sx={{
        ".MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiDialog-paper": {
          backgroundColor: "rgb(249 250 251)",
          borderRadius: "0.5rem",
        },
      }}
    >
      <DialogTitle className="font-medium px-4">
        Get values for env variables
      </DialogTitle>
      <List sx={{ pt: 0 }}>
        {envVariables.map((variable) => (
          <ListItem disableGutters key={variable}>
            <ListItemButton>
              <ListItemText primary={variable} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Dialog>
  );
}

export default function SimpleDialogDemo() {
  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button
        variant="outlined"
        onClick={handleClickOpen}
        className="normal-case p-3 text-gray-500 dark:text-gray-300 dark:hover:bg-gray-800 rounded-lg dark:border-white/25 dark:hover:border-white/75"
      >
        Get values for env variables
      </Button>
      <SimpleDialog open={open} onClose={handleClose} />
    </div>
  );
}
