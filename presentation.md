# Hotels.com Customer Churn Analysis
## Executive Presentation for Leadership Team

**Duration:** 20 minutes  
**Audience:** Senior Executives  
**Presenter:** [Name]  
**Date:** [Insert Date]

---

## Slide 1: Title Slide

### Content
- **Title:** Understanding & Reducing Customer Churn at Hotels.com
- **Subtitle:** Data-Driven Insights for Customer Retention Strategy
- **Presenter:** [Name], Data Science Team
- **Date:** [Date]

### Visual
- Clean, professional layout with Hotels.com branding
- Subtle background image of a hotel or travel scene
- Company logo prominently displayed

### Speaker Notes
> "Good morning everyone, and thank you for taking the time to join me today. I'm [Name] from the Data Science team, and I'm excited to share some really important findings about our customer retention challenges.
>
> Over the next 20 minutes, I'm going to walk you through what we've learned about why customers leave us—and more importantly, what we can do about it. We've analysed nearly 700,000 booking records, built predictive models, and identified some very clear patterns that I think will change how we think about customer retention.
>
> By the end of this presentation, you'll understand exactly which factors drive churn, you'll see how we can predict which customers are at risk, and I'll share five concrete recommendations that I believe can meaningfully reduce our churn rate. So let's dive in."

---

## Slide 2: The Business Challenge

### Content
**Why We're Here:**
- High customer churn rate observed
- Customers not rebooking within 6 months of last stay
- Significant revenue at risk from customer attrition

**What Leadership Asked Us:**
1. Which factors contribute most to churn?
2. Can we predict who will churn?
3. What can we do to reduce it?

### Visual
- Simple text layout with key questions highlighted
- Optional: Icon graphics representing each question (magnifying glass for analysis, crystal ball for prediction, toolkit for solutions)

### Speaker Notes
> "So let's start with why we're here. The leadership team rightly identified that we have a churn problem—too many of our customers are making one booking and never coming back. When we define churn as 'no repeat booking within 6 months of checkout,' we're seeing numbers that represent a significant revenue opportunity.
>
> You asked us three questions: First, what's actually causing this? Which factors matter most? Second, can we get ahead of this—can we predict who's about to leave before they do? And third—and this is really the actionable part—what can we actually do to fix it?
>
> I'm pleased to say we have answers to all three, and they're quite clear. Let me show you what we found."

---

## Slide 3: Our Analytical Approach

### Content
**Data Analysed:**
- 689,744 booking records
- ~XXX,XXX unique customers
- Period: August 2018 – July 2019

**Methodology:**
1. Exploratory analysis of all factors
2. Statistical significance testing
3. Machine learning model development
4. Customer risk segmentation

### Visual
- Flowchart showing: Data Collection → EDA → Statistical Testing → Model Building → Insights
- Small data icons representing volume
- Timeline graphic for the date range

### Speaker Notes
> "Let me quickly walk you through how we approached this. We pulled data on nearly 700,000 bookings—that's every booking over about a year's worth of data. For each booking, we have rich information: who the customer is, how they found us, what they did on our website, their loyalty status, whether they cancelled, and crucially, whether they ever came back.
>
> We started with exploratory analysis—really getting to know the data, looking at distributions, identifying patterns. Then we moved to statistical testing to validate which factors are genuinely significant versus just noise. Finally, we built machine learning models to see how well we can actually predict churn and to understand the relative importance of each factor.
>
> So everything I'm about to show you isn't just interesting patterns—it's statistically validated and predictively useful."

---

## Slide 4: Current Churn Landscape

### Content
**Overall Churn Rate:** XX.X%

**What This Means:**
- X in Y customers don't return
- Represents $XXM in potential lifetime value at risk annually
- Opportunity for significant improvement

### Visual
- **Large donut/pie chart** showing Churned (red) vs Retained (green) split
- The churn percentage should be prominently displayed in the centre
- Animated if possible to draw attention

### Speaker Notes
> "Alright, let's look at where we stand. This chart shows our current churn situation, and I want you to focus on that red segment. That represents XX% of our customers who booked with us and then... disappeared. They didn't come back within six months.
>
> Now, let me put that in perspective. If we assume an average customer lifetime value of [X], that red segment represents roughly [Y] million pounds in revenue that's walking out the door every year. Every percentage point we can shave off that churn rate translates directly to retained revenue and customer lifetime value.
>
> The encouraging thing is that this isn't random. As I'll show you, there are very clear patterns in who churns and why. And if there are patterns, there are solutions."

---

## Slide 5: Key Finding #1 – Customer Type is Critical

### Content
**The Pattern:**
- New Customers: ~XX% churn rate
- Existing Customers: ~XX% churn rate
- Gap: ~XX percentage points

**The Insight:** First-time customers are significantly more likely to leave

### Visual
- **Side-by-side bar chart** comparing churn rates
- New customers bar in red/orange (higher churn)
- Existing customers bar in green (lower churn)
- Clear labels showing the percentage difference
- Horizontal dashed line showing overall average

### Speaker Notes
> "Now, let me take you through our top findings, starting with the single biggest factor: customer type. Look at this chart. On the left, we have new customers—people making their first-ever booking with Hotels.com. On the right, existing customers—people who've booked with us before.
>
> The difference is striking. New customers have a churn rate of around XX%, while existing customers are down at XX%. That's a XX percentage point gap. This tells us something really important: the hardest part of the customer journey is getting someone from their first booking to their second booking.
>
> Think about it like a funnel. We spend a lot of money acquiring new customers—marketing, advertising, promotions. But if we can't convert them to a second booking, that acquisition cost never pays off. The customer who books twice? They're dramatically more likely to become a loyal, long-term customer.
>
> So our first strategic priority should be: how do we help new customers have such a great experience that they can't wait to book again?"

---

## Slide 6: Key Finding #2 – Loyalty Tier Matters Enormously

### Content
**Churn Rate by Loyalty Status:**
- Non-members (Tier 0): ~XX%
- Base members (Tier 1): ~XX%
- Silver/Gold (Tier 2): ~XX%

**Key Takeaway:** Each loyalty tier step reduces churn significantly

### Visual
- **Descending bar chart** showing churn rate decreasing as loyalty tier increases
- Colour gradient from red (Tier 0) → yellow (Tier 1) → green (Tier 2)
- Percentage labels on each bar
- Arrow graphic showing "decreasing churn" direction

### Speaker Notes
> "The second major factor is loyalty programme membership, and honestly, this one is really encouraging because it validates that our loyalty programme works.
>
> Look at these three bars. Non-members—customers who haven't signed up for our loyalty programme—have the highest churn rate at XX%. Base members drop to XX%. And our Silver and Gold members? Down to just XX%.
>
> That's not a coincidence. What this tells us is that loyalty programme membership genuinely creates stickiness. When customers accumulate points, earn rewards, and feel recognised, they come back.
>
> But here's the strategic question this raises: if loyalty membership is so protective against churn, why do we have so many non-members? How do we make it easier and more compelling to join? And how do we help Base members progress to Silver faster?
>
> Every customer we move up the loyalty ladder becomes dramatically less likely to leave us for a competitor."

---

## Slide 7: Key Finding #3 – Cancellation is an Early Warning Signal

### Content
**The Data:**
- Customers who cancelled a booking: ~XX% churn
- Customers who never cancelled: ~XX% churn

**Insight:** Cancellation is a strong predictor of future churn—and an intervention opportunity

### Visual
- **Two-bar comparison chart** with stark contrast
- Non-cancellers in green, cancellers in red
- Consider adding a "warning sign" icon next to the cancellation bar
- Show the percentage point difference prominently

### Speaker Notes
> "Now this third finding is perhaps the most immediately actionable. Look at the difference between customers who have cancelled a booking versus those who haven't.
>
> Customers who cancel are nearly twice as likely to churn completely. Now, why might that be? Well, cancellation often signals something went wrong—maybe they found a better deal elsewhere, maybe their plans changed and we didn't make rebooking easy enough, maybe they were dissatisfied with something in the booking process.
>
> But here's the opportunity: cancellation is an observable event. It happens in our system, we know exactly when it happens, and we know who it happens to. That means cancellation is an early warning signal we can actually act on.
>
> When a customer cancels, we shouldn't just process the cancellation and move on. We should be reaching out, understanding why, offering alternatives, making it easy to rebook. Because if we don't intervene at that moment, there's a good chance we've lost them for good."

---

## Slide 8: Key Finding #4 – Engagement Predicts Retention

### Content
**Low Engagement = High Churn:**
- Fewer pages viewed
- Less time on website
- Fewer destinations searched
- Higher bounce rates

**High Engagement = Low Churn:**
- More property pages viewed
- Longer browsing sessions
- Multiple destinations explored

### Visual
- **Split comparison graphic** or **two-column layout**
- Left side (red-tinted): "Low Engagement" with down arrows and metrics
- Right side (green-tinted): "High Engagement" with up arrows and metrics
- Or: Scatter plot showing engagement metric vs churn rate with trend line

### Speaker Notes
> "The fourth pattern relates to how customers interact with our website before and during booking. And this one is intuitive but important to quantify.
>
> Customers who churn tend to have what I'd call 'shallow' engagement with our platform. They spend less time browsing, they look at fewer properties, they don't explore multiple destinations. It's almost like they're just transacting rather than genuinely engaging with Hotels.com as a platform.
>
> In contrast, customers who return tend to have 'deep' engagement. They browse extensively, compare properties, look at different destinations. They're investing time in our platform, which suggests they see us as their go-to resource for hotel bookings.
>
> What does this mean practically? Two things. First, we should look at our UX—are we making it easy and enjoyable for customers to explore? Second, customers who book very quickly with minimal engagement might need extra nurturing because they're higher risk. They haven't built a relationship with us yet."

---

## Slide 9: Platform & Channel Insights

### Content
**By Platform:**
- App users: Lowest churn
- Desktop: Moderate churn
- Mobile Web: Higher churn

**By Marketing Channel:**
- Direct traffic: Lowest churn
- Paid search: Variable
- Affiliates/Meta: Higher churn

### Visual
- **Grouped bar chart** showing churn rate by platform (top)
- **Grouped bar chart** showing churn rate by channel (bottom)
- Colour-coded by churn level (green to red gradient)
- Include sample sizes to show reliability

### Speaker Notes
> "We also looked at platform and acquisition channel effects. A couple of interesting patterns here.
>
> On platform: customers who book through our app have noticeably lower churn than desktop or mobile web users. Why? Probably because downloading and using the app represents a higher level of commitment. These customers have literally given us space on their phone—they're invested in using Hotels.com.
>
> On marketing channels: customers who come to us directly—typing hotels.com into their browser—have lower churn than those we acquire through paid channels or affiliates. That makes sense too. Direct visitors already know us and chose us; paid acquisition customers might be more price-sensitive or less brand-loyal.
>
> Now, I'm not saying we should stop paid acquisition—it's essential for growth. But we should recognise that customers from different channels may need different retention approaches. And driving app adoption could be a meaningful retention lever."

---

## Slide 10: Statistical Validation

### Content
**All Key Findings Are Statistically Significant (p < 0.001)**

| Factor | Chi-Square | Effect Size |
|--------|-----------|-------------|
| Customer Type | Very High | Large |
| Loyalty Tier | Very High | Large |
| Cancellation | Very High | Medium-Large |
| Platform | High | Medium |
| Marketing Channel | High | Medium |

### Visual
- **Summary table** with significance indicators
- Use stars (***) or checkmarks to indicate significance levels
- Consider a simple bar showing effect size comparison
- Green checkmarks for validated factors

### Speaker Notes
> "Now, I know some of you might be thinking: are these patterns real, or could they be statistical noise? Great question, and it's exactly why we ran rigorous significance tests on every factor.
>
> This table summarises the results. Every single key finding I've shared is statistically significant at the 99.9% confidence level. The p-values are essentially zero—these patterns are not random.
>
> We also looked at effect size, which tells us how practically meaningful the effects are, not just whether they're statistically significant. Customer type and loyalty tier have large effects—they move the needle substantially. Cancellation, platform, and channel have medium effects—still meaningful and actionable.
>
> So you can have confidence that the patterns I'm describing are real and will persist if we act on them."

---

## Slide 11: Our Predictive Model

### Content
**Three Models Tested:**

| Model | ROC-AUC | What It Tells Us |
|-------|---------|------------------|
| Logistic Regression | ~0.70 | Interpretable odds ratios |
| **Random Forest** | **~0.76** | **Best overall performance** |
| Gradient Boosting | ~0.75 | Strong predictive power |

**Selected:** Random Forest for deployment

### Visual
- **ROC curve plot** showing all three models overlaid
- Random Forest curve highlighted/thicker
- Diagonal reference line for "random chance"
- AUC values in legend
- Clear visual showing RF as the winner

### Speaker Notes
> "To operationalise these insights, we built machine learning models that can score individual customers based on their likelihood to churn. We tested three different approaches.
>
> Logistic Regression is the most interpretable—it gives us nice, clean odds ratios that tell us exactly how each factor affects churn probability. Random Forest is an ensemble method that captures complex patterns and interactions. Gradient Boosting is another ensemble approach known for strong predictive performance.
>
> This chart shows the ROC curves—without getting too technical, the closer to the top-left corner, the better. Random Forest came out on top with an AUC of about 0.76. What does that mean in practical terms? If I show the model two customers—one who will churn and one who won't—it will correctly identify which is which about 76% of the time.
>
> That's good enough to drive real business value. It means we can score our customer base and identify who's at risk before they leave."

---

## Slide 12: Feature Importance – What Drives the Model

### Content
**Top 10 Factors (Ranked by Predictive Power):**
1. Customer Type (New vs Existing)
2. Maximum Loyalty Tier Achieved
3. Cancellation Rate
4. Total Number of Bookings
5. Average Visit Duration
6. Average Property Pages Viewed
7. Platform Preference
8. Pay Now Rate
9. Average Bounce Visits
10. Marketing Channel

### Visual
- **Horizontal bar chart** showing feature importance scores
- Bars sorted descending by importance
- Top 3-4 bars highlighted or in different colour
- Importance values labelled on each bar
- Clear title: "What Matters Most for Predicting Churn"

### Speaker Notes
> "This chart shows what's driving the model's predictions—which factors carry the most weight. And reassuringly, it aligns with everything we've discussed.
>
> At the top: customer type. Whether someone is new or existing is the single most predictive factor. Then loyalty tier, cancellation history, and total bookings. These four factors alone account for a huge portion of the model's predictive power.
>
> Website engagement metrics—visit duration, property pages viewed, bounce visits—are also meaningful. Platform and marketing channel contribute as well.
>
> What I love about this chart is that it validates our earlier analysis and gives us a clear prioritisation. If we want to reduce churn, we should focus our efforts on the factors at the top of this list. That's where we'll get the biggest bang for our buck."

---

## Slide 13: Customer Risk Segmentation

### Content
**Four Risk Categories:**

| Category | % of Customers | Actual Churn Rate |
|----------|----------------|-------------------|
| 🟢 Low Risk | XX% | ~XX% |
| 🟡 Medium Risk | XX% | ~XX% |
| 🟠 High Risk | XX% | ~XX% |
| 🔴 Critical Risk | XX% | ~XX% |

### Visual
- **Stacked bar or pie chart** showing customer distribution by risk category
- Colour-coded: Green → Yellow → Orange → Red
- Side panel showing actual churn rate for each segment
- Visual emphasis on High/Critical risk segments

### Speaker Notes
> "Using our model, we've scored every customer and grouped them into four risk categories. Let me show you how this works.
>
> Low Risk customers—shown in green—have a churn probability under 30%. These are our healthiest customers. They tend to be existing, loyal members who engage deeply with our platform.
>
> Medium Risk—in yellow—have probabilities between 30% and 50%. They need monitoring but aren't urgent.
>
> High Risk—in orange—are between 50% and 70%. These customers are more likely than not to churn. They should be prioritised for retention efforts.
>
> And Critical Risk—in red—are above 70%. These customers are almost certainly going to leave unless we intervene.
>
> Look at how the actual churn rates validate the model. Low Risk customers really do have low churn. Critical Risk customers really do have very high churn. The model is working.
>
> This segmentation lets us allocate our retention resources efficiently. Rather than treating everyone the same, we can focus our efforts where they'll have the greatest impact."

---

## Slide 14: Recommendation #1 – First-Booking Experience Programme

### Content
**Initiative:** Comprehensive New Customer Onboarding

**Target:** All first-time customers

**Tactics:**
- Personalised welcome email within 24 hours of booking
- Post-stay feedback request with easy response mechanism
- "Book Again" incentive: 10-15% off second booking within 30 days
- Loyalty programme introduction with sign-up bonus

**Expected Impact:** ⭐⭐⭐ HIGH

### Visual
- **Customer journey flowchart** showing touchpoints:
  First Booking → Welcome Email → Stay → Feedback Request → Rebooking Incentive → Second Booking
- Icons for each touchpoint
- Timeline below showing when each interaction happens

### Speaker Notes
> "Alright, let's talk solutions. I have five recommendations, and I'll start with the one addressing our biggest churn driver: new customer attrition.
>
> We're calling this the 'First-Booking Experience Programme.' The goal is to nurture new customers from their first booking to their second—because once they book twice, they're dramatically more likely to become long-term customers.
>
> Here's how it works. Within 24 hours of their first booking, they get a personalised welcome email—not generic marketing, but a genuine thank-you with helpful information about their upcoming stay. After they check out, we proactively ask for feedback. This does two things: it shows we care about their experience, and it gives us early warning if something went wrong.
>
> Then—and this is the key intervention—we offer a meaningful incentive to book again within 30 days. Something like 10-15% off their next stay. We also introduce the loyalty programme with a sign-up bonus, because we know loyalty members have dramatically lower churn.
>
> This programme addresses our number one churn driver head-on. I'd rate the expected impact as high."

---

## Slide 15: Recommendation #2 – Loyalty Programme Enhancement

### Content
**Initiative:** Accelerate Loyalty Tier Progression

**Target:** Non-members and Base tier members

**Tactics:**
- Prominent loyalty promotion during booking flow
- Reduced threshold for Base tier qualification
- Milestone rewards at 2nd, 5th, 10th booking
- Exclusive flash sales for members only
- Birthday/anniversary recognition

**Expected Impact:** ⭐⭐⭐ HIGH

### Visual
- **Loyalty tier ladder graphic** showing progression
- Arrows indicating "acceleration" opportunities
- Before/after comparison of tier thresholds
- Icons for each reward type

### Speaker Notes
> "The second recommendation focuses on our loyalty programme, which we know is highly protective against churn.
>
> The strategic question is: how do we get more customers into the programme, and how do we help them progress faster? Because the data is clear—every tier upgrade reduces churn risk significantly.
>
> Here's what I'm proposing. First, we need to promote loyalty benefits more prominently during the booking flow. Right now, I think many customers don't fully understand what they're missing. Second, let's lower the barrier to Base tier. If someone is close, let's find a reason to bump them up—that tier transition creates stickiness.
>
> I also love the idea of milestone rewards. When someone makes their second booking, their fifth booking, their tenth booking—let's celebrate that. Send them something special. Make them feel recognised. And exclusive member-only deals create FOMO for non-members and reward existing members.
>
> Small touches like birthday recognition also matter. They make customers feel like more than just a transaction number. All of this builds emotional connection, and emotional connection drives loyalty."

---

## Slide 16: Recommendation #3 – Cancellation Recovery Campaign

### Content
**Initiative:** Structured Post-Cancellation Intervention

**Target:** Customers who cancel any booking

**Tactics:**
- Automated outreach within 4-6 hours of cancellation
- Short survey: "Help us understand" (3 questions max)
- Rebooking incentive valid for 7 days
- Flexible rebooking policy promotion
- Escalation to human contact for high-value customers

**Expected Impact:** ⭐⭐⭐ HIGH

### Visual
- **Timeline/flowchart** showing:
  Cancellation Event → 4-6 hours → Automated Email + Survey → Day 3 → Reminder → Day 7 → Final Offer
- Decision tree showing escalation for high-value customers
- Sample email mockup if available

### Speaker Notes
> "Third recommendation: we need to get much better at handling cancellations. Right now, when a customer cancels, we process it and... that's it. They're gone. But we know cancellation is a strong predictor of churn—so this is exactly when we should be engaging, not disengaging.
>
> Here's the campaign I'm proposing. Within 4-6 hours of a cancellation—while we're still top of mind—the customer receives a personalised message. Not salesy, but genuinely caring. Something like: 'We're sorry your plans changed. We'd love to understand what happened so we can do better.'
>
> We include a very short survey—three questions maximum—to understand the cancellation reason. Did they find a better price? Did their travel plans change? Was there something wrong with the booking process?
>
> We also include a rebooking incentive—maybe 10% off—valid for 7 days. Creating some urgency. And we highlight our flexible rebooking policies.
>
> For high-value customers—our frequent bookers—we should escalate to human contact. A personal call from our customer success team can make a huge difference.
>
> This is about converting a negative moment into a retention opportunity. The customer who was about to leave could become even more loyal if we handle this well."

---

## Slide 17: Recommendation #4 – Engagement-Based Interventions

### Content
**Initiative:** Proactive Engagement for Low-Activity Customers

**Target:** Customers with low website engagement patterns

**Tactics:**
- Personalised destination recommendations via email
- "Complete Your Search" retargeting for abandoned sessions
- Push notifications for saved/searched destinations
- UX improvements to encourage deeper exploration
- Gamification elements (e.g., "You've explored 5 destinations!")

**Expected Impact:** ⭐⭐ MEDIUM

### Visual
- **Before/after UX mockups** showing engagement improvements
- Email template example with personalised recommendations
- Push notification example
- Engagement funnel showing dropout points

### Speaker Notes
> "Fourth recommendation addresses the engagement gap. We know that customers who engage deeply with our platform—browsing lots of properties, spending time researching—are more likely to return. So how do we help customers engage more?
>
> Part of this is proactive outreach. If someone searched for Paris hotels but didn't book, we should follow up with curated recommendations. 'Still thinking about Paris? Here are 5 properties we think you'd love.' Personalised, relevant, helpful.
>
> For abandoned sessions—someone who was browsing and then left—retargeting can bring them back. 'You were looking at hotels in Barcelona. Ready to continue?'
>
> Push notifications for our app users can highlight deals in destinations they've shown interest in. But we need to be thoughtful here—notification fatigue is real.
>
> There's also a UX component. Are we making it easy and enjoyable to explore? Can we add elements that encourage deeper engagement? Maybe even light gamification—'You've explored 5 destinations this month!'
>
> I've rated this as medium impact because it's less direct than the first three recommendations, but it's still meaningful and helps build the platform habit."

---

## Slide 18: Recommendation #5 – Predictive Churn Scoring System

### Content
**Initiative:** Deploy Real-Time Risk Scoring

**Implementation:**
- Integrate model into CRM and marketing platforms
- Daily/weekly score refresh for all customers
- Automated trigger campaigns based on risk level
- Dashboard for retention team monitoring
- Monthly model performance review

**Expected Impact:** ⭐⭐⭐ HIGH (Enabler for all other initiatives)

### Visual
- **System architecture diagram** showing:
  Data Sources → ML Model → Risk Scores → CRM/Marketing Automation → Campaigns
- Dashboard mockup showing risk distribution
- Alert notification examples for high-risk customers

### Speaker Notes
> "My fifth and final recommendation is about operationalising everything we've discussed. We've built a model that can predict churn—but it only creates value if we actually use it.
>
> What I'm proposing is a real-time scoring system integrated with our CRM and marketing automation. Every customer gets a churn risk score, updated regularly. That score flows into our marketing platforms and triggers appropriate campaigns automatically.
>
> High-risk customer identified? They automatically enter a retention workflow—maybe a special offer, maybe a check-in email, maybe a survey to understand if something's wrong. This happens without manual intervention.
>
> We'd also build a dashboard for the retention team to monitor risk distribution, track interventions, and see what's working. And we'd review model performance monthly to ensure it stays accurate.
>
> I've rated this as high impact because it's an enabler. It makes all our other retention initiatives smarter and more targeted. Instead of batch-and-blast campaigns, we can do precision retention. That's a fundamental shift in capability."

---

## Slide 19: Implementation Roadmap

### Content
**Phase 1: Quick Wins (Months 1-3)**
- Launch cancellation recovery campaign
- Implement first-booking email series
- Begin scoring infrastructure development

**Phase 2: Scale Up (Months 4-6)**
- Deploy predictive scoring system
- Roll out loyalty programme enhancements
- A/B test retention incentive levels

**Phase 3: Optimise (Months 7-12)**
- Full personalisation by risk segment
- Expand to all channels
- Continuous optimisation based on results

### Visual
- **Gantt chart or timeline** showing three phases
- Key milestones marked with diamonds
- Colour-coded by initiative
- "We Are Here" marker at start
- Clear delivery dates for each initiative

### Speaker Notes
> "So how do we actually make this happen? Here's a realistic roadmap.
>
> Phase 1 is about quick wins—things we can do in the next three months with relatively low effort. The cancellation recovery campaign can be set up quickly with our existing email platform. The first-booking email series is similar. Meanwhile, our tech team starts building the infrastructure for the scoring system.
>
> Phase 2, months four through six, is where we scale up. The scoring system goes live. We roll out the loyalty programme changes. We start A/B testing to optimise our incentive levels—is 10% the right discount, or should it be 15%? Or maybe a different type of reward entirely?
>
> Phase 3, the back half of the year, is about optimisation and expansion. By this point we have data on what's working. We can get more sophisticated with personalisation. We extend successful approaches to all channels.
>
> This phased approach manages risk, allows for learning, and delivers value incrementally rather than asking you to wait a year for results."

---

## Slide 20: Expected Business Impact

### Content
**Conservative Projections (12-Month Horizon):**

| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| Overall Churn Rate | XX% | XX% | -X pp |
| New Customer Retention | XX% | XX% | +X pp |
| Loyalty Programme Enrolment | XX% | XX% | +X pp |

**Financial Impact:**
- Incremental retained revenue: £X.XM - £X.XM
- Programme investment: £XXX,XXX
- Projected ROI: X:1 to X:1

### Visual
- **Waterfall chart** showing current churn → interventions → target churn
- ROI calculation graphic
- Confidence range bars on projections
- Clear "bottom line" number highlighted

### Speaker Notes
> "Now, what does all this mean for the business? Let me walk you through our projections—and I want to be clear, these are conservative estimates.
>
> If we successfully implement these initiatives, we project we can reduce our overall churn rate by X percentage points within twelve months. For new customer retention specifically, we're targeting an improvement of X points.
>
> What does that translate to in pounds and pence? Based on our customer lifetime value calculations, reducing churn by X points means retaining roughly X thousand additional customers per year. At an average LTV of £X, that's £X million in incremental revenue.
>
> Against an investment of approximately £XXX thousand for technology, campaigns, and incentives, we're looking at an ROI in the range of X to 1.
>
> Now, I've given you a range here because there's always uncertainty. But even at the conservative end of that range, this is a compelling business case. Customer retention is almost always more cost-effective than acquisition, and these numbers bear that out."

---

## Slide 21: Summary & Call to Action

### Content
**What We've Learned:**
1. ✅ New customers and non-members are highest risk
2. ✅ Cancellation is a critical early warning signal
3. ✅ Our model can identify at-risk customers with ~76% accuracy
4. ✅ Five targeted initiatives can meaningfully reduce churn

**What We're Asking For:**
1. Approval to proceed with Phase 1 initiatives
2. Budget allocation of £XXX,XXX
3. Cross-functional project team assignment
4. Monthly progress review cadence

**Questions?**

### Visual
- Clean summary layout with checkmarks
- Clear "Ask" section highlighted
- Contact information
- "Questions?" prompt with discussion visual

### Speaker Notes
> "So let me bring this all together.
>
> We came into this analysis with three questions from leadership. Which factors drive churn? We now know: customer type, loyalty tier, and cancellation behaviour are the big three, with engagement and channel also playing meaningful roles.
>
> Can we predict churn? Yes. Our Random Forest model achieves 76% AUC and enables us to segment customers by risk level before they leave.
>
> What can we do about it? Five initiatives: first-booking experience programme, loyalty enhancement, cancellation recovery, engagement interventions, and a predictive scoring system. Together, these address our key churn drivers systematically.
>
> What I'm asking for today is approval to move forward with Phase 1, budget allocation to support the initiatives, a cross-functional team—we'll need marketing, product, tech, and CX involved—and a commitment to monthly progress reviews so we can course-correct as we learn.
>
> I'm confident that with executive support, we can make meaningful progress on customer retention this year. And I'm happy to take any questions you have.
>
> Thank you for your time and attention."

---

## Appendix Slides

### A1: Detailed Methodology
- Data preprocessing steps
- Feature engineering details
- Model selection criteria
- Cross-validation approach

### A2: Full Model Performance Metrics
- Complete classification reports
- Precision-recall curves
- Calibration plots
- Learning curves

### A3: Statistical Test Details
- Chi-square test results with full values
- T-test results for numerical variables
- Effect size calculations
- Multiple comparison corrections

### A4: Data Dictionary
- Complete field definitions
- Value coding explanations
- Data quality notes
- Sample size by segment

### A5: Sensitivity Analysis
- Impact of different churn definitions
- Model stability across time periods
- Feature importance consistency

---

## Backup Q&A Talking Points

**Q: "How confident are we in the model predictions?"**
> "Great question. Our model has a ROC-AUC of about 0.76, which means it significantly outperforms random guessing. In practical terms, if I take one customer who churned and one who didn't, the model correctly identifies which is which about three-quarters of the time. That's strong enough to drive value while acknowledging no model is perfect. We should think of it as a prioritisation tool—helping us focus retention efforts where they're most likely to succeed—rather than a crystal ball."

**Q: "Won't offering discounts to prevent churn erode our margins?"**
> "It's a valid concern, and one we need to manage carefully. A few thoughts: First, the cost of a retention discount is almost always less than the cost of acquiring a new customer. Second, we shouldn't offer discounts to everyone—the risk scoring lets us target just the customers who need it. Third, we can test different incentive types—it might not always need to be a discount. Loyalty points, free upgrades, or exclusive access might work just as well for some segments. We'll A/B test to find the most cost-effective approaches."

**Q: "How often should we retrain the model?"**
> "I'd recommend quarterly retraining to keep the model current with evolving customer behaviour. Booking patterns, competitive dynamics, and customer expectations all shift over time. We should also set up monitoring to alert us if model performance degrades between retraining cycles. If we see accuracy dropping, we can trigger an earlier refresh."

**Q: "What about customers who churn because of price? Can we really retain them?"**
> "You're right that pure price shoppers are harder to retain—if someone is only loyal to the lowest price, they'll always be at risk. But a few points: First, not all churners are price-driven. Many leave due to poor experiences, lack of engagement, or simply forgetting about us. Those are retainable. Second, even price-sensitive customers can be influenced by switching costs—loyalty points accumulated, saved preferences, familiarity with the platform. Our loyalty programme creates those switching costs. Third, our model will naturally identify the price-loyal customers as lower-probability saves, so we won't waste resources on truly unretainable customers."

**Q: "How does this integrate with our existing marketing campaigns?"**
> "The scoring system should integrate with our marketing automation platform. Risk scores become another attribute we can use for segmentation and targeting. High-risk customers might be excluded from certain acquisition campaigns and instead routed to retention workflows. We can also use risk scores to personalise messaging—a high-risk customer might see different content than a low-risk one. The key is making the scores accessible to the teams who manage campaigns, which is why CRM integration is part of the Phase 1 plan."

**Q: "What if customers feel over-contacted or stalked?"**
> "Absolutely something we need to manage. I'd recommend several guardrails: First, frequency caps on retention communications—no customer should receive more than X messages per week regardless of their risk score. Second, preference centres where customers can control communication frequency. Third, value-first messaging—every communication should offer something useful, not just ask for a booking. Fourth, A/B testing to ensure our retention efforts don't have unintended negative effects. We want to be helpful, not annoying."
