# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.1.9
### Added
  - Had to update the PINECONE_KEY to PINECONE_API_KEY (2023-12-28)

## 1.1.8
### Added
  - feature/70-keys-list-to-set (2023-12-28)

## 1.1.6
### Added
  - feature/64-retricts-what-can-be-passed-to-settings-and-history (2023-12-26)

## 1.1.5
### Added
  - feature/61-index-becomes-index_name (2023-12-26)

## 1.1.4
### Fixed
  - Commit: e932202568d3c9654c82565530ff362610482bb3 | Adds better error handling for tools in agent

## 1.1.3
### Fixed
  - Fixing some vectorstore routes | https://github.com/promptengineers-ai/core/pull/59

## 1.1.2
### Added
  
  - feature/55-update-ollama-rag-chat (2023-12-17) 

## 1.1.1
### Fixed
  - feature/rag-chat-fixed-to-not-be-agent (2023-12-13) 

## 1.1.0
### Added
  - feature/50-adds-settings-and-updates-history-endpoints (2023-12-10) 
  - Not backwards compatible, affects changes to the history api based on settings api but I'm most likely only one using so staying on v1."

## 1.0.2
### Fixed
  - Needed to add llms/services/__init__.py 

## 1.0.1
### Fixed
  - Needed to add core/__init__.py

## 1.0.0
### Added
  - feaure/47-segment-modules-based-on-dependencies (2023-12-09)

## 0.1.24
### Added
  - feature/44-system-prompt-template-api (2023-12-09)
  
#### Skipped a few versions in between

## 0.1.15
### Added
  - feature/lambda-loader (2023-12-03)

## 0.1.14
### Added
  - feature/23-equips-streaming-with-retreival-agent (2023-12-03)

## 0.1.13
### Added
  - feature/18-add-get-controller-to-retrieval-routes (2023-12-1)

## 0.1.12
### Fixed
  - bugfix/16-fix-async-iterator-chat-controller (2023-11-26)

## 0.1.11
### Fixed
  - bugfix/13-schema-extra-to-json-schema-extra (2023-11-26)

## 0.1.10
### Fixed
  - bugfix/11-update-function-call-line (2023-11-26)

## 0.1.9
### Added
  - feature/5-agent-action-message-multiple-steps (2023-11-25)
### Fixed
  - bugfix/13-schema-extra-to-json-schema-extra (2023-11-26)

## 0.1.8
### Added 
  - feature/5-agent-actions-returned (2023-11-25)
  
## 0.1.6
### Added 
  - Includes changes from integrating with Saas App, allows for flexibility.

## 0.1.5
### Added 
  - feature/4-remove-default-basic-middlware (2023-11-23)
  
## 0.1.4
### Added 
  - feature/2-add-changelog-update-script (2023-11-23)
