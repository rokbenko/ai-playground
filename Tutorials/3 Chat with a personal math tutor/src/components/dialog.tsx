import React from 'react';
import Button from '@mui/material/Button';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import DialogTitle from '@mui/material/DialogTitle';
import Dialog from '@mui/material/Dialog';
import LoadingButton from '@mui/lab/LoadingButton';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';

export interface DialogProps {
  open: boolean;
  onClose: () => void;
}

function SimpleDialog(props: DialogProps) {
  const { open: dialogOpen, onClose } = props;

  const [loadingAssistants, setLoadingAssistants] = React.useState(false);
  const [loadingThreads, setLoadingThreads] = React.useState(false);

  const [extractedInfoForAssistants, setExtractedInfoForAssistants] =
    React.useState([]);
  const [extractedInfoForThread, setExtractedInfoForThread] = React.useState<
    { id: any; created_at: any }[]
  >([]);

  const handleClose = () => {
    setLoadingAssistants(false);
    setLoadingThreads(false);
    onClose();
  };

  const getAllAssistants = async (e: any) => {
    setLoadingAssistants(true);
    e.preventDefault();

    setLoadingAssistants(true);

    try {
      const response = await fetch(`/api/listAssistants`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
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

  const getAllThreads = async (e: any) => {
    e.preventDefault();

    setLoadingThreads(true);

    try {
      const response = await fetch(`api/createThread`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
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
      setLoadingThreads(false);
    }
  };

  return (
    <Dialog
      onClose={handleClose}
      open={dialogOpen}
      sx={{
        '.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiDialog-paper': {
          backgroundColor: 'rgb(249 250 251)',
          borderRadius: '0.5rem',
          padding: '1rem',
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
              '&.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary':
                {
                  color: 'white',
                  backgroundColor: 'rgba(52,53,65,1)',
                  borderColor: 'rgba(255, 255, 255, 0.5)',
                  borderRadius: '0.5rem',
                },
            }}
          >
            List all assistants
          </LoadingButton>
        </ListItem>
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
              '&.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary':
                {
                  color: 'white',
                  backgroundColor: 'rgba(52,53,65,1)',
                  borderColor: 'rgba(255, 255, 255, 0.5)',
                  borderRadius: '0.5rem',
                },
            }}
          >
            Create a new Thread
          </LoadingButton>
        </ListItem>
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
                    <TableCell>{thread.id}</TableCell>
                    <TableCell>
                      {formatUnixTimestamp(
                        thread.created_at,
                        'si-SL',
                        'Europe/Ljubljana'
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
  );
}

const formatUnixTimestamp = (
  timestamp: number,
  locale: string,
  timeZone: string
) => {
  const milliseconds = timestamp * 1000;
  return new Intl.DateTimeFormat(locale, {
    year: 'numeric',
    month: 'numeric',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric',
    timeZone: timeZone,
  }).format(new Date(milliseconds));
};

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
          '&.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary':
            {
              color: 'rgba(0, 0, 0, 0.8)',
              fontWeight: '600',
              backgroundColor: 'rgba(255, 255, 255, 1)',
              borderColor: 'rgba(255, 255, 255, 0.5)',
              borderRadius: '0.5rem',
            },
          '&.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary:hover':
            {
              backgroundColor: 'rgba(255, 255, 255, 0.8)',
            },
        }}
      >
        Get values for env variables
      </Button>
      <SimpleDialog
        open={open}
        onClose={handleClose}
      />
    </div>
  );
}
