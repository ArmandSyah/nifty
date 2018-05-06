import React, { PureComponent } from 'react';
import logo from './logo.svg';
import './App.css';
import { Paper } from 'material-ui';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

import SentenceMaker from './components/SentenceMaker'
import SentenceDisplay from './components/SentenceDisplay'

const style = {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    textAlign: 'center'
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
