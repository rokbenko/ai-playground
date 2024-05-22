// Imports
import { useRef, useEffect } from "react";

// Functional component for auto-resizing text area
export default function useAutoResizeTextArea() {
  // Setting up reference to the text area
  const textAreaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    // Resizing the text area based on its content
    if (textAreaRef.current) {
      textAreaRef.current.style.height = "24px";
      textAreaRef.current.style.height = `${textAreaRef.current.scrollHeight}px`;
    }
  }, [textAreaRef]);

  return textAreaRef;
}
