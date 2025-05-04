# Synthesis Assistant

A powerful command-line tool powered by Gemini AI to assist in retrosynthetic analysis for organic chemistry research and education.

## Overview

Synthesis Assistant is an interactive command-line interface that leverages Google's Gemini AI to provide expert guidance on retrosynthesis planning. This tool is designed to help chemists, researchers, and students analyze complex molecules, identify disconnection points, and develop practical synthetic routes with appropriate reagents and reaction conditions.

## Features

- **Interactive Retrosynthesis Planning**: Analyze target molecules and generate multiple viable synthetic routes
- **Expert Chemistry Knowledge**: Access AI-assisted insights on disconnection strategies, reagent selection, and reaction conditions
- **Practical Approach**: Considers protecting group strategies, reaction feasibility, and laboratory implementation
- **User-Friendly Interface**: Color-coded terminal output for improved readability
- **Conversation Management**: Maintain context while clearing previous exchanges

## Installation

### Prerequisites

- Python 3.10+
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/annczer/MLprojekt17.git
   cd MLprojekt17
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   If a requirements.txt file is not present, you can install the dependencies manually:
   ```bash
   pip install requests colorama
   ```

## Getting Started

### Obtaining a Gemini API Key

1. Visit the [Google AI Studio](https://aistudio.google.com/) website
2. Sign in with your Google account
3. Go to the API section from the navigation menu
4. Create a new API key or use an existing one
5. Copy your API key for use with the Synthesis Assistant

### Running the Application

There are two ways to provide your API key:

#### Option 1: Using environment variables

```bash
export GEMINI_API_KEY="your-api-key-here"
python3 synthesis_assistant.py
```

#### Option 2: Using command-line arguments

```bash
python3 synthesis_assistant.py --api-key "your-api-key-here"
```

## Usage

Once the application is running, you can interact with the Synthesis Assistant in the following ways:

1. **Requesting synthesis routes**:
   - Provide a SMILES string of your target molecule
   - Describe the molecular structure you want to synthesize
   - Ask for specific transformations or functional group manipulations

2. **Special commands**:
   - Type `exit` or `quit` to end the session
   - Type `/clear` to start a new conversation while preserving the chemistry context

## Example Interaction

```
Welcome to Gemini Retrosynthesis Assistant!
I'm an expert synthetic chemist who can help design retrosynthetic pathways.
Describe your target molecule or provide a SMILES string, and I'll suggest synthesis routes.
Type 'exit' or 'quit' to end the conversation.
Type '/clear' to start a new conversation while preserving the chemist context.

You: How would you synthesize aspirin starting from benzene?

Chemist: To synthesize aspirin (acetylsalicylic acid) from benzene, we need to introduce a carboxylic acid group and a hydroxyl group at the ortho position, then acetylate the hydroxyl group. Here's a practical retrosynthetic approach:

[Detailed synthesis explanation follows...]
```

## Technical Details

Synthesis Assistant works by:

1. Establishing a specialized context for the Gemini AI model to act as an expert synthetic chemist
2. Maintaining a conversation history to provide consistent and contextually relevant responses
3. Communicating with the Gemini API through a secure REST interface
4. Formatting responses for optimal readability in the terminal environment

## Limitations

- The quality of suggestions depends on the clarity of the input and the capabilities of the underlying AI model
- The system cannot perform actual experiments or verify results experimentally
- Complex molecules with unusual functional groups might receive less accurate guidance
- Internet connectivity is required to communicate with the Gemini API

## Contributing

Contributions to improve Synthesis Assistant are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google's Gemini AI for providing the underlying AI capabilities
- The open-source Python community for the supporting libraries
- Organic chemistry researchers whose work informs the retrosynthesis strategies

---

For questions or support, please open an issue on the GitHub repository: [https://github.com/annczer/MLprojekt17/issues](https://github.com/annczer/MLprojekt17/issues)
