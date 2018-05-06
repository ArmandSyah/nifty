import React, { PureComponent } from 'react';
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
    constructor(props) {
        super(props);
        this.state = {
            average: 0
        }
    }
    getSentiment = (sentence) => {
        const data = fetch('/sentence', {
            body: JSON.stringify({ sentence }),
            credentials: 'same-origin',
            headers: {
                'user-agent': 'nifty-react',
                'content-type': 'application/json'
            },
            method: 'POST'
        })
            .then(response => response.json())
            .catch(error => console.error(error));
        data.then(result => {
            const average = result.average
            this.setState({ average })
        });

    }
    renderTitle() {
        return (
            <h1>Nifty</h1>
        )
    }
    render() {
        const { average } = this.state;
        console.log(average);
        return (
            <MuiThemeProvider>
                <Paper style={style} zDepth={5}>
                    {this.renderTitle()}
                    <SentenceDisplay />
                    <SentenceMaker getSentiment={this.getSentiment} />
                </Paper>
            </MuiThemeProvider>
        );
    }
}

export default App;
