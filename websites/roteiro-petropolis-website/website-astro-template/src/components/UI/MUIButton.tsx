import React from 'react';
import Button from '@mui/material/Button';
import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#ff9800',
    },
    mode: 'dark',
  },
});

interface Props {
  label: string;
  variant?: 'text' | 'outlined' | 'contained';
  onClick?: () => void;
}

export const MUIButton: React.FC<Props> = ({ label, variant = 'contained', onClick }) => {
  return (
    <ThemeProvider theme={theme}>
      <Button variant={variant} color="primary" onClick={onClick} sx={{ borderRadius: '12px', fontWeight: 'bold' }}>
        {label}
      </Button>
    </ThemeProvider>
  );
};

export default MUIButton;
