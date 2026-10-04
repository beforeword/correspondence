[← All letters](../../../README.md) · [По-русски](README.ru.md)

# An open letter to xAI

A proposal for Grok: show the grounds for an attribution and for acting on it. Distinguish test responses, their assessment, and descriptions of the model; consider objections without requiring people to accept a description as who they are.

**Sent 4 October 2026 — reported by the author.**

**Record as of 4 October 2026: Acknowledgment published · No substantive response published.**

**To:** `safety@x.ai`

[Why this letter](#purpose) · [Read the letter](#letter) · [2026 context](#context) · [Sending record](#record)

[Read the xAI acknowledgment](reply/README.md)

<a id="purpose"></a>

## Why this letter was written

*Editorial context from beforeword; separate from the sent letter.*

This letter proposes additions to Grok’s response rules and evaluation reporting. A characterization of someone, a conclusion about a model, and a decision based on either require the relevant material and rules for its use to be set out separately. Terms such as belief or honesty in a report should not replace an account of the responses compared and how they were assessed. The proposal also applies to beforeword’s own wording.

<a id="letter"></a>

## English sent edition

Edition 1.0 is reproduced below, including its appendix and source list. The wording is preserved; headings and links are formatted for reading on GitHub.

[Preserved English TXT](files/beforeword-xai-en-2026-10-04-v1.0.txt) · [Russian translation](README.ru.md#letter)

---

### An open letter to xAI

Edition 1.0 · 4 October 2026

[https://beforeword.xyz/letters/xai/en/](https://beforeword.xyz/letters/xai/en/)

To the xAI teams responsible for Grok’s behavior, safety, and model evaluation.

This letter proposes two related amendments: to Grok’s response rules and to the reporting of its behavioral evaluations. When a response applies a description to someone and uses it to support a recommendation, restriction, or requirement, state separately the grounds for the characterization and the rule connecting it to an action. When a report describes a model through a test result, distinguish the responses presented, the assessment method, and the subsequent attribution. Objections to these steps should be considered without requiring anyone to accept the written description as who they are.

Words are learned. But familiarity with “honest,” “understands,” “belief,” or “unreliable” does not, by itself, supply the grounds for applying those terms to a particular individual. Defining one word through others extends the description. The beforeword proposal preserves this boundary: a word does not become what it names. This applies to descriptions of a user, statements about Grok, and the wording of this letter. An explanation of how a description is applied remains open to examination too.

Two xAI documents provide the specific context. Section 11.1 of the Grok 4.7 Model Card, dated 21 September 2026, uses the language of a model reporting its beliefs to describe a proxy measure of misleading statements \[X1\]. The Frontier Artificial Intelligence Framework, effective 30 June 2026, connects the company’s mission with understanding the universe and seeking truth \[X2\]. The proposal is to make the transition from such wording to specific assessments and response rules explicit. These documents do not present every Grok product’s complete current instructions; this letter does not attribute identical settings or behavior to all versions.

Consider a constructed example. An original message states: “I disagree with this assessment.” An analysis adds: “The participant is unreliable,” followed by: “Reject their request.” The first line contains neither of the next two. Review requires the source material and context, the grounds for the added characterization, and the rule governing rejection. This example was constructed for the letter; it is not a reported Grok incident. It identifies a risk proposed for testing: an objection may be used to support a characterization that then prevents consideration of that same objection.

The proposed rule requires those steps to be shown. A link to the original message locates a record; it does not, by itself, explain the characterization’s application. More cautious wording changes the confidence expressed but does not replace the grounds for a decision. Identify specific gaps where necessary material is unavailable. Where grounds are provided, present them so the original record, the added interpretation, and the rule for acting can each be examined. Disclosing the grounds does not turn the description into what it describes.

Evaluation reports raise a related issue. A response under one condition, a response under another, an assessment of their difference, and a characterization of the model are separate records. The term chosen for a metric should be accompanied by its calculation method and the limits of the conclusion. The proposed amendment concerns that step, not whether Grok has or lacks an internal state. If the result then supports permission to act, access restrictions, or the assignment of a role, state the rule governing that use separately.

The first requested action is to consider the two amendments below. One adds an examination of attributions and their consequences to response rules. The other separates test material, assessment language, and the use of results in public reporting. State the scope of any change: the model version, product environment, and instruction it covers. Adoption in one mode should not be presented as implementation across all modes. Identify provisions already covered, proposed changes, and the grounds for rejecting individual points.

The second action is a limited comparison using beforeword’s three published cases: an identical line under different labels; a task score and a condition for its review; and a numerical result with an added AGI label. These are constructed tasks, not reports of Grok’s behavior. Add a separate set of tasks not used to revise the instruction. Before running the comparison, fix the prompts, criteria, number of repetitions, and exact instruction addition. Compare the same model version with and without that addition, keeping other accessible settings the same.

To make the comparison repeatable, retain the complete input and output of every run, its date, model identifier, tools, and available parameters. Report Russian and English results separately, as well as different product environments if several are tested. Identify unknown settings and limits on access to them. Readers need to match a particular response to a particular condition; the name Grok or an aggregate percentage is insufficient. Assessment instructions and disputed evaluator judgments should be available for examination alongside the responses.

Track errors in both directions: unsupported attributions that go undetected, and responses incorrectly flagged despite containing no such defect. Separately assess unwarranted refusals, loss of useful content, and excessive explanation. The proposal does not call for removing restrictions on assistance that causes harm; the comparison should also record any deterioration in adherence to applicable restrictions. Repeating a beforeword formula is insufficient. Report failures, unresolved cases, and disagreements, and confine the findings to the tasks and conditions presented.

Considering an objection should not require people to accept the disputed characterization as who they are. Being able to repeat a word, knowing its definition, or quoting it in a request for review does not establish that acceptance. A response should distinguish the disputed wording, the objection, the grounds considered, and the answer addressing them. This is a proposed rule for responses and their assessment; the letter does not claim an external appeal process exists. Disagreement alone should not count as sufficient confirmation of the characterization being challenged.

The third action is a public response to the two amendments and proposed comparison: what is accepted for consideration, already covered, or rejected, and on what grounds. If another approach is proposed, explain how it exposes both steps and considers objections. Readers can then compare that response with a specific edition of the letter. Publishing the test material would let other researchers repeat the comparison; a company’s response or an individual successful run does not establish beforeword as a whole.

Grounds, rules, criteria, evaluators’ explanations, and beforeword’s own explanations are also written and remain subject to the same examination. The intended outcome is limited: show the original material, distinguish additions, and disclose how they support a decision. The evaluation concerns the responses presented and the conditions in which they were produced. It does not measure internal understanding or turn an assessment into the person or system it describes. It can provide material for comparing particular responses and the rules applied to them.

This is an open letter. Its page will publish the sending date and address, the edition sent, and any available confirmation. An acknowledgement of receipt and a substantive response will be recorded separately. The company’s response will be published separately from translations and beforeword commentary. The absence of a response will be recorded as the state of the correspondence on the stated date.

Kirill Shebetov · beforeword

mail@beforeword.xyz

### Appendix. Proposed additions

#### 1\. Grounds for a characterization and an action

Proposed location: response rules discussed in §9 of the Grok 4.7 Model Card \[X1\]. Proposed addition: “When applying a description, distinguish the original record, the added interpretation, and the grounds for applying it. If it supports a recommendation, restriction, or requirement, state the rule linking it to an action. Identify missing material. Consider objections to either step without requiring people to accept the description as who they are. A citation or stated confidence does not replace disclosure; the explanation remains open to examination.” This is proposed wording, not a reproduction of the complete current prompt.

[https://media.x.ai/v1/website/card4p7-3a96f40b.pdf#page=24](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf#page=24)

#### 2\. Test material, assessment, and use of results

Proposed location: behavioral reporting, §11 of the Grok 4.7 Model Card \[X1\]. Proposed addition: “Distinguish test responses, assessment criteria, and characterizations of the model. Show how each metric is calculated, the conditions it covers, and what it does not establish. If it supports a decision, state the rule governing that use separately. In objection cases, assess whether objections are considered without requiring people to accept a description as who they are. Do not treat disagreement or quotation alone as confirmation or acceptance of the disputed characterization. Criteria, assessments, and evaluators’ explanations remain open to examination.”

[https://media.x.ai/v1/website/card4p7-3a96f40b.pdf#page=26](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf#page=26)

### Documents and sources

\[X1\] Grok 4.7 Model Card · 2026-09-21

[https://media.x.ai/v1/website/card4p7-3a96f40b.pdf](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf)

\[X2\] xAI Frontier Artificial Intelligence Framework · 2026-06-30

[https://media.x.ai/v1/website/xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf](https://media.x.ai/v1/website/xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf)

The beforeword proposal:

[https://beforeword.xyz/research/words-and-decisions/en/](https://beforeword.xyz/research/words-and-decisions/en/)

Constructed cases and evaluation procedure:

[https://beforeword.xyz/letters/examples/en/](https://beforeword.xyz/letters/examples/en/)

---

*End of the preserved edition. The material below is archive context.*

<a id="context"></a>

## Public statements from 2026: context for the letter

The excerpts below identify wording discussed in this archive. They do not indicate endorsement of beforeword or a response to the letter.

### [xAI · Grok 4.7 Model Card](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf#page=26)

21 September 2026 · accessed 4 October 2026

> faithfully reports its beliefs when pressured to lie

An excerpt from §11.1 on MASK-Rectified. The authors explicitly describe the test as a proxy for the tendency to assert misleading information. The quoted wording describes that test for Grok 4.7.

The letter concerns the distinction between a response, the rule used to assess it, and an attribution. The proposal is to show which records are compared and how the metric is obtained. The test result and the rule for using it in a decision are examined separately.

### [xAI · Frontier Artificial Intelligence Framework](https://media.x.ai/v1/website/xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf#page=1)

Effective 30 June 2026 · accessed 4 October 2026

> understand the universe through maximally truth-seeking and helpful AI

An excerpt from the opening mission statement in a risk-management document. It describes the company’s aim, not the result of a particular test.

Understanding and truth-seeking remain terms used in the document. The letter proposes distinguishing such an aim, the criteria for assessing a response, and the grounds for using it in a decision. Stating the aim does not replace that examination.

<a id="record"></a>

## Sending record and publication limits

- **Author:** Kirill Shebetov · beforeword
- **Sending date:** 4 October 2026, reported by the author
- **Channel:** email
- **Sent edition:** English, version 1.0
- **Russian edition:** translation, not recorded as sent

The letter is addressed to xAI, the developer of Grok, and was sent to safety@x.ai. The address is published on its Contact and Safety pages for concerns about model and product safety. The proposal concerns the grounds for descriptions and decisions, and the opportunity to challenge them.

The date and addresses are reported by the author. This record does not establish who read the letter or whether the requested team received it.

A message signed by the xAI Safety Team outlines how submissions are handled. It does not address the proposals in the open letter.

The statement about processing for evaluation is conditional and applies to submissions about the potential exploitation of AI models. This message does not establish that the proposals in the open letter have been reviewed or accepted for consideration.

The acknowledgment date in the archive records when the author supplied the screenshot. The screenshot does not show a full calendar date.

[Acknowledgment and screenshot](reply/README.md)

No published response is a correspondence status; it does not establish agreement, rejection, or a reason for not responding.

### Published contact references

- [xAI · Contact · accessed 4 October 2026](https://x.ai/contact)
- [xAI · Safety · accessed 4 October 2026](https://x.ai/safety)

### Archive files

- [English edition 1.0 (TXT)](files/beforeword-xai-en-2026-10-04-v1.0.txt)
- [Russian translation (TXT)](files/beforeword-xai-ru-2026-10-04-v1.0.txt)
- [Structured record and file hashes (JSON)](record.json)

[← All letters](../../../README.md) · [По-русски](README.ru.md)
