# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.0.8-rc.9
### Changed
  - feature/101-publish-chunking-status-to-redis (2024-03-19)

## 0.0.8-rc.8
### Changed
  - feature/97-add-support-for-assistant-starter-query-templates (2024-03-09) 
### Fixed
  - bugfix/98-add-search-type-and-search-kwargs (2024-03-11)

## 0.0.8-rc.7
### Fixed
  - Updated setup.py dependencies for langsmith==0.0.87 and langchain-community==0.0.20 

## 0.0.8-rc.6
### Fixed
  - Updated setup.py dependencies for langsmith==0.0.87 and langchain-community==0.0.20 

## 0.0.8-rc.2
### Fixed
  - feature/94-application-token-defaults

## 0.0.8-rc.1
### Fixed
  - bugfix/remove-singleton-from-mongo-service

## 0.0.7
### Changed
  - Same as 0.0.6, could not overwrite pypi version

## 0.0.6
### Changed
  - Fixes for file loader

## 0.0.5
### Changed
  - Model updats for gpt4turbo and embeddings

## 0.0.4
### Changed
  - Need to add notes

## 0.0.3
### Changed
  - Release (2024-01-21)

## 0.0.3-rc.2
### Changed
  - feature/87-cleans-up-document-loading-functionality (2024-01-20)

## 0.0.3-rc.1
### Changed
  - feature/85-detach-chat-from-controllers-and-user-repo (2024-01-18)

## 0.0.2
### Changed
  - Not enough considerations were being made for multi-app support. In light would like to go back to
    0.0.x patches in order to take what's been learned from build POC apps into making this repository
    truly ubiquitous no matter what app it is installed into. Striving to make 0.1.0 stable and does not
    lock in users to functionality they do not want, but instead striving to make concepts easier to compose.

## 1.1.14
### Fixed
  - Forgot to resolve in fastapi/retreival (2024-01-03)

## 1.1.13
### Fixed
  - bugfix/81-vectorstore-file-fix-args (2024-01-03)

## 1.1.12
### Added
  - feature/15-can-pass-tools-and-user-repo-to-include-router (2024-01-01)

## 1.1.11
### Added
  - feature/76-updates-params-for-ability-to-fetch-from-other-properties (2023-12-31)

## 1.1.10
### Added
  - Updates HistoryController constructor to include a user_id as request alternative. (2023-12-30)

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
