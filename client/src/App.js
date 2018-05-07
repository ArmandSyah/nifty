import React, { PureComponent } from 'react';
import './App.css';
import { Paper, CircularProgress } from 'material-ui';
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
    gridRow: '2 / 3',
    justifySelf: 'center',
    paddingBottom: '20px'
}

class App extends PureComponent {
    constructor(props) {
        super(props);
        this.state = {
            average: '0',
            loadingRating: false,
            sentence: ''
        }
    }
    getSentiment = (sentence) => {
        this.setState({ loadingRating: true })
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
            const average = Number.parseFloat(result.average).toFixed(3);
            this.setState({ average, loadingRating: false, sentence });
        });

    }

    renderTitle() {
        return (
            <div className="nifty-title">Nifty</div>
        )
    }

    renderRating() {
        const { average, loadingRating, sentence } = this.state;
        if (loadingRating) {
            return (
                <div>
                    <CircularProgress size={60} />
                </div>
            )
        }
        return (<div className="sentence-display">
            <div className="sentence">Sentence: {sentence}</div>
            <div>Sentiment Score: {average}</div>
        </div>)
    }

    render() {
        const { average } = this.state;
        console.log(average);
        return (
            <MuiThemeProvider>
                <div className="nifty">
                    {this.renderTitle()}
                    <Paper style={style} zDepth={5}>
                        <SentenceDisplay />
                        {this.renderRating()}
                        <SentenceMaker getSentiment={this.getSentiment} />
                    </Paper>
                </div>
            </MuiThemeProvider>
        );
    }
}

export default App;
