import React, { PureComponent } from 'react';
import logo from './logo.svg';
import './App.css';
import { Paper } from 'material-ui';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

import SentenceMaker from './components/SentenceMaker'
import SentenceDisplay from './components/SentenceDisplay'

const style = {
    width: '50%',
    display: 'flex',
    alignSelf: 'center',
    flexDirection: 'column',
    justifyContent: 'center',
    textAlign: 'center',
    backgroundColor: '#d6829e',
    position: 'fixed',
    top: '33%',
    left: '25%'
}

class App extends PureComponent {
    renderTitle() {
        return (
            <h1>Nifty</h1>
        )
    }
    render() {
        return (
            <MuiThemeProvider>
                <Paper style={style} zDepth={5}>
                    {this.renderTitle()}
                    <SentenceDisplay />
                    <SentenceMaker />
                </Paper>
            </MuiThemeProvider>
        );
    }
}

export default App;
