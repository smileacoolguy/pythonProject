
"""
import numpy as np
import tensorflow as tf
from keras.api.models import Sequential
from keras.api.layers import LSTM, Dense
from keras.api.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split



# Sample dataset of HTML elements and corresponding XPaths
dataset = [
    {'element': '<html><head></head></htmllllll>', 'xpath': '/html/head'},
    {'element': '<html1><head></head></html1>', 'xpath': '/html1/head'},
    #{'element': '<div class="container"></div>', 'xpath': '//div[@class="container"]'},
    # Add more samples...
]

# Preprocess the dataset
max_length = max(len(sample['element']) for sample in dataset)
elements = [sample['element'] for sample in dataset]
xpaths = [sample['xpath'] for sample in dataset]

# Create vocabulary and convert elements and XPaths to numerical sequences
vocabulary = sorted(set(''.join(elements)))
char_to_index = {char: index + 1 for index, char in enumerate(vocabulary)}
x_encoded = [[char_to_index[char] for char in element] for element in elements]
y_encoded = [[char_to_index[char] for char in xpath] for xpath in xpaths]

# Pad sequences to a fixed length
x_padded = pad_sequences(x_encoded, maxlen=max_length, padding='post', value=0)
y_padded = pad_sequences(y_encoded, maxlen=max_length, padding='post', value=0)

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_padded, y_padded, test_size=0.2, random_state=42)

# Define the model architecture
model = Sequential()
model.add(LSTM(128, input_shape=(max_length, len(vocabulary) + 1)))
model.add(Dense(max_length, name="2", activation='softmax', input_shape=(x_train.shape[0],)))
#model.add(tf.keras.layers.Dense(256, input_shape=(x_train.shape[1],), activation='sigmoid'))

# Compile and train the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=12, batch_size=32, validation_data=(x_test, y_test), shuffle=False)

# Generate XPath predictions
sample_element = '<div class="example"></div>'
sample_encoded = [char_to_index[char] for char in sample_element]
sample_padded = pad_sequences([sample_encoded], maxlen=max_length, padding='post', value=0)
prediction = model.predict(sample_padded)
predicted_xpath_encoded = np.argmax(prediction, axis=2)[0]
predicted_xpath = ''.join([vocabulary[index - 1] for index in predicted_xpath_encoded])

print("Predicted XPath:", predicted_xpath)

"""

#https://stackoverflow.com/questions/65305528/add-a-dimension-to-a-tensorflow-tensor

from lxml import etree

def generate_xpath(element):
    xpath = etree.ElementTree(element).getpath(element)
    return xpath

# Example HTML
html = """
<html>
  <body>
    <div id="container">
      <h1>Title</h1>
      <p>Paragraph 1</p>
      <p>Paragraph 2</p>
    </div>
  </body>
</html>
"""

html =""" 
    
    <!DOCTYPE html>
    
    
        <html itemscope itemtype="https://schema.org/QAPage" class="html__responsive " lang="en">
    
        <head>
    
            <title>keras - Stateful LSTM Tensorflow Invalid Input_h Shape Error - Stack Overflow</title>
            <link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196">
            <link rel="apple-touch-icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
            <link rel="image_src" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a"> 
            <link rel="search" type="application/opensearchdescription+xml" title="Stack Overflow" href="/opensearch.xml">
            <link rel="canonical" href="https://stackoverflow.com/questions/64159777/stateful-lstm-tensorflow-invalid-input-h-shape-error" />
        <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
            <meta property="og:type" content= "website" />
            <meta property="og:url" content="https://stackoverflow.com/questions/64159777/stateful-lstm-tensorflow-invalid-input-h-shape-error"/>
            <meta property="og:site_name" content="Stack Overflow" />
            <meta property="og:image" itemprop="image primaryImageOfPage" content="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded" />
            <meta name="twitter:card" content="summary"/>
            <meta name="twitter:domain" content="stackoverflow.com"/>
            <meta name="twitter:title" property="og:title" itemprop="name" content="Stateful LSTM Tensorflow Invalid Input_h Shape Error" />
            <meta name="twitter:description" property="og:description" itemprop="description" content="I am experimenting with stateful LSTM on a time-series regression problem by using TensorFlow. I apologize that I cannot share the dataset.&#xA;Below is my code.&#xA;train_feature = train_feature.reshape((" />
        <script id="webpack-public-path" type="text/uri-list">https://cdn.sstatic.net/</script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script defer src="https://cdn.sstatic.net/Js/third-party/npm/@stackoverflow/stacks/dist/js/stacks.min.js?v=d5f780ae3281"></script>
        <script src="https://cdn.sstatic.net/Js/stub.en.js?v=01af928a07d1"></script>
    
        <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Shared/stacks.css?v=5017f4b5c9a3">
        <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Sites/stackoverflow/primary.css?v=9871e6bf989a">
    
    
        
                <link rel="alternate" type="application/atom+xml" title="Feed for question &#x27;Stateful LSTM Tensorflow Invalid Input_h Shape Error&#x27;" href="/feeds/question/64159777">
            <script>
                StackExchange.ready(function () {
    
                        StackExchange.using("snippets", function () {
                            StackExchange.snippets.initSnippetRenderer();
                        });
                        
                    StackExchange.using("postValidation", function () {
                        StackExchange.postValidation.initOnBlurAndSubmit($('#post-form'), 2, 'answer');
                    });
    
    
                    StackExchange.question.init({showAnswerHelp:true,showTrendingSortLaunchPopover:false,showTrendingSortPostLaunchPopover:false,totalCommentCount:1,shownCommentCount:1,enableTables:true,questionId:64159777});
    
                    styleCode();
    
                        StackExchange.realtime.subscribeToQuestion('1', '64159777');
                        StackExchange.using("gps", function () { StackExchange.gps.trackOutboundClicks('#content', '.js-post-body'); });
    
    
                });
            </script>
    
            
            
            
            <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Shared/Channels/channels.css?v=487caf0a5e80">
    
            
            
    
    
        <script type="application/json" data-role="module-args" data-module-name="Shared/options.mod">{"options":{"locale":"en","serverTime":1715767546,"routeName":"Questions/Show","stackAuthUrl":"https://stackauth.com","networkMetaHostname":"meta.stackexchange.com","site":{"name":"Stack Overflow","description":"Q\u0026A for professional and enthusiast programmers","isNoticesTabEnabled":true,"enableNewTagCreationWarning":true,"insertSpaceAfterNameTabCompletion":false,"id":1,"cookieDomain":".stackoverflow.com","childUrl":"https://meta.stackoverflow.com","negativeVoteScoreFloor":null,"enableSocialMediaInSharePopup":true,"protocol":"https"},"user":{"fkey":"4a4af90770b3a1e583cccae29b6b66c55d0409a14103bc5d312f983c6775f325","tid":"b32f93c7-431d-4bc8-86c0-561000283060","rep":0,"isAnonymous":true,"isAnonymousNetworkWide":true,"ab":{"collectives_survey":{"v":"coso_survey","g":1}}},"events":{"postType":{"question":1},"postEditionSection":{"title":1,"body":2,"tags":3}}}}</script>
    <script type="application/json" data-role="module-args" data-module-name="Shared/settings.mod">{"settings":{"paths":{"jQueryUIJSPath":"https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.0/jquery-ui.min.js","jQueryUICSSPath":"https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.0/themes/smoothness/jquery-ui.css"},"legal":{"useCustomConsent":false,"oneTrustTCFConfigId":"c3d9f1e3-55f3-4eba-b268-46cee4c6789c"},"elections":{"opaVoteResultsBaseUrl":"https://www.opavote.com/results/"},"comments":{},"snippets":{"snippetsEnabled":true,"renderDomain":"stacksnippets.net"},"subscriptions":{"defaultFreemiumMaxTrueUpSeats":50,"defaultBasicMaxTrueUpSeats":250,"defaultMaxTrueUpSeats":1000},"userMessaging":{"showNewFeatureNotice":true},"tags":{},"flags":{"allowRetractingFlags":true,"allowRetractingCommentFlags":true},"mentions":{"maxNumUsersInDropdown":50},"markdown":{"enableTables":true},"site":{"allowImageUploads":true,"enableImgurHttps":true,"styleCode":true,"stacksEditorPreviewEnabled":true,"forceHttpsImages":true,"enableUserHovercards":true},"accounts":{"currentPasswordRequiredForChangingStackIdPassword":true},"auth":{},"intercom":{"appId":"inf0secd"},"search":{},"activationExperiment":{"showNewSignupModal":true},"questions":{"enableQuestionTitleLengthLiveWarning":true,"maxTitleSize":150,"enableSavesFeature":true,"questionTitleLengthStartLiveWarningChars":50}}}</script>
    <script>StackExchange.init();</script>
    
        <script>
            StackExchange.using.setCacheBreakers({"Js/adops.en.js":"6da43f5e0a84","Js/ask.en.js":"","Js/begin-edit-event.en.js":"20edbaccceae","Js/copy-transpiled.en.js":"e0eb0f70fc72","Js/events.en.js":"","Js/explore-qlist.en.js":"2b1f34938b8b","Js/full-anon.en.js":"9731ccb8b344","Js/full.en.js":"1fed9427f1f5","Js/highlightjs-loader.en.js":"510e2f94c2bf","Js/inline-tag-editing.en.js":"8517756a2cb6","Js/keyboard-shortcuts.en.js":"40f19073ece0","Js/markdown-it-loader.en.js":"5818ef89ff9d","Js/mentions-transpiled.en.js":"e9226a7ec13c","Js/moderator.en.js":"cda9cd5883e6","Js/postCollections-transpiled.en.js":"11a255fe9394","Js/post-validation.en.js":"243bf7d290a3","Js/question-editor.en.js":"","Js/review-v2-transpiled.en.js":"07991cc48f78","Js/revisions.en.js":"47b4d5ac24c9","Js/stacks-editor.en.js":"7c86c325ec61","Js/tageditor.en.js":"4d22c6090e5a","Js/tageditornew.en.js":"4554c63a5fa6","Js/tagsuggestions.en.js":"bd6ec908f2a7","Js/unlimited-transpiled.en.js":"f26a1d5f3365","Js/wmd.en.js":"7239639e7e32","Js/snippet-javascript-codemirror.en.js":"ae1dcf38deb7"});
            StackExchange.using("gps", function() {
                 StackExchange.gps.init(true);
            });
        </script>
        <noscript id="noscript-css"><style>body,.s-topbar{margin-top:1.9em}</style></noscript>
        </head>
        <body class="question-page unified-theme">
    
            
    <div id="signup-modal-container"></div>
    <script type="application/json" data-role="module-args" data-module-name="islands/signup-modal/index.mod">{"ContainerElementId":"signup-modal-container","FKey":"4a4af90770b3a1e583cccae29b6b66c55d0409a14103bc5d312f983c6775f325","TriggerEvent":"signupModalShow","OauthInPopup":false,"ReturnUrl":"https://stackoverflow.com/questions/64159777/stateful-lstm-tensorflow-invalid-input-h-shape-error","ReturnUrlForPopup":"https://stackoverflow.com/users/after-signup/oauth-only","SiteName":"Stack Overflow","SiteLogoPath":"https://cdn.sstatic.net/Sites/stackoverflow/Img/icon-48.png?v=b7e36f88ff92","AuthProviders":["Google","GitHub"]}</script>
    <script defer src="https://cdn.sstatic.net/Js/webpack-chunks/71.en.js?v=df900d976cca"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/8184.en.js?v=c565036a497f"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/6828.en.js?v=4c50b1e12ff1"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/4607.en.js?v=731109be5b3d"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/8825.en.js?v=cc3faab55723"></script><script defer src="https://cdn.sstatic.net/Js/islands/signup-modal.en.js?v=cbc38bc9f51c"></script>
    
    <script defer>
        dispatchEvent(new CustomEvent("openSignupModal"));
    </script>
        
            <div id="one-tap-container"></div>
    <script type="application/json" data-role="module-args" data-module-name="islands/one-tap/index.mod">{"ContainerElementId":"one-tap-container","FKey":"4a4af90770b3a1e583cccae29b6b66c55d0409a14103bc5d312f983c6775f325","GoogleClientId":"717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com","Autoselect":false,"ReturnUrl":"https%3a%2f%2fstackoverflow.com%2fquestions%2f64159777%2fstateful-lstm-tensorflow-invalid-input-h-shape-error","OneTapNotShownEvent":"one-tap-not-shown"}</script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/71.en.js?v=df900d976cca"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/3724.en.js?v=55eb4850442a"></script><script defer src="https://cdn.sstatic.net/Js/islands/one-tap.en.js?v=e26f990f9143"></script>    <div id="notify-container"></div>
        <div id="custom-header"></div>
            
    
    <header class="s-topbar ps-fixed t0 l0 js-top-bar">
        <a href="#content" class="s-topbar--skip-link">Skip to main content</a>
        <div class="s-topbar--container">
                <a href="#" class="s-topbar--menu-btn js-left-sidebar-toggle" role="menuitem" aria-haspopup="true" aria-controls="left-sidebar" aria-expanded="false"><span></span></a>
                <div class="topbar-dialog leftnav-dialog js-leftnav-dialog dno">
                    <div class="left-sidebar js-unpinned-left-sidebar" data-can-be="left-sidebar" data-is-here-when="sm"></div>
                </div>
                    <a href="https://stackoverflow.com" class="s-topbar--logo js-gps-track"
               data-gps-track="top_nav.click({is_current:false, location:2, destination:8}); homelogo_nav.click({location:2})">
                        <span class="-img _glyph">Stack Overflow</span>
                    </a>
    
    
    
                <ol class="s-navigation" role="presentation">
    
                        <li class="md:d-none">
                            <a href="https://stackoverflow.co/" class="s-navigation--item js-gps-track"
                       data-gps-track="top_nav.products.click({location:2, destination:7})"
                       data-ga="[&quot;top navigation&quot;,&quot;about menu click&quot;,null,null,null]">About</a>
                        </li>
    
                    <li>
                        <a href="#"
                       class="s-navigation--item js-gps-track js-products-menu"
                       aria-controls="products-popover"
                       data-controller="s-popover"
                       data-action="s-popover#toggle"
                       data-s-popover-placement="bottom"
                       data-s-popover-toggle-class="is-selected"
                       data-gps-track="top_nav.products.click({location:2, destination:1})"
                       data-ga="[&quot;top navigation&quot;,&quot;products menu click&quot;,null,null,null]">
                            Products
                        </a>
                    </li>
    
                        <li class="md:d-none">
                            <a href="https://stackoverflow.co/teams/ai/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=top-nav-bar&amp;utm_content=overflowai" class="s-navigation--item js-gps-track"
                            data-gps-track="top_nav.products.click({location:2, destination:10})"
                            data-ga="[&quot;top navigation&quot;,&quot;learn more - overflowai&quot;,null,null,null]">OverflowAI</a>
                        </li>
    
                </ol>
                <div class="s-popover ws2 mtn2 p0"
                 id="products-popover"
                 role="menu"
                 aria-hidden="true">
                    <div class="s-popover--arrow"></div>
                    <ol class="list-reset s-anchors s-anchors__inherit">
                        <li class="m6">
                            <a href="/questions" class="bar-sm p6 d-block h:bg-black-225 js-gps-track"
                           data-gps-track="top_nav.products.click({location:2, destination:2})"
                           data-ga="[&quot;top navigation&quot;,&quot;public qa submenu click&quot;,null,null,null]">
                                <span class="fs-body1 d-block">Stack Overflow</span>
                                <span class="fs-caption d-block fc-black-400">Public questions &amp; answers</span>
                            </a>
                        </li>
                        <li class="m6">
                            <a href="https://stackoverflow.co/teams/" class="bar-sm p6 d-block h:bg-black-225 js-gps-track"
                           data-gps-track="top_nav.products.click({location:2, destination:3})"
                           data-ga="[&quot;top navigation&quot;,&quot;teams submenu click&quot;,null,null,null]">
                                <span class="fs-body1 d-block">Stack Overflow for Teams</span>
                                <span class="fs-caption d-block fc-black-400">Where developers &amp; technologists share private knowledge with coworkers</span>
                            </a>
                        </li>
                        <li class="m6">
                            <a href="https://stackoverflow.co/talent/" class="bar-sm p6 d-block h:bg-black-225 js-gps-track"
                           data-gps-track="top_nav.products.click({location:2, destination:5})"
                           data-ga="[&quot;top navigation&quot;,&quot;talent submenu click&quot;,null,null,null]">
                                <span class="fs-body1 d-block">Talent</span>
                                <span class="fs-caption d-block fc-black-400">
                                    Build your employer brand
                                </span>
                            </a>
                        </li>
                        <li class="m6">
                            <a href="https://stackoverflow.co/advertising/" class="bar-sm p6 d-block h:bg-black-225 js-gps-track"
                           data-gps-track="top_nav.products.click({location:2, destination:6})"
                           data-ga="[&quot;top navigation&quot;,&quot;advertising submenu click&quot;,null,null,null]">
                                <span class="fs-body1 d-block">Advertising</span>
                                <span class="fs-caption d-block fc-black-400">Reach developers &amp; technologists worldwide</span>
                            </a>
                        </li>
                        <li class="bt bc-black-200 py6 px6 bbr-md">
                            <a href="https://stackoverflow.co/labs/" class="bar-sm p6 d-block h:bg-black-225 js-gps-track"
                           data-gps-track="top_nav.products.click({location:2, destination:7})"
                           data-ga="[&quot;top navigation&quot;,&quot;labs submenu click&quot;,null,null,null]">
                                <span class="fs-body1 d-block">Labs</span>
                                <span class="fs-caption d-block fc-black-400">The future of collective knowledge sharing</span>
                             </a>
                        </li>
                        <li class="bg-black-100 bt bc-black-200 py6 px6 bbr-md">
                            <a href="https://stackoverflow.co/" class="fc-black-400 d-block py6 px6 h:fc-black-600 js-gps-track"
                           data-gps-track="top_nav.products.click({location:2, destination:7})"
                           data-ga="[&quot;top navigation&quot;,&quot;about submenu click&quot;,null,null,null]">About the company</a>
                        </li>
                    </ol>
                </div>
    
    
                    <form id="search" role="search" action=/search class="s-topbar--searchbar js-searchbar " autocomplete="off">
                            <div class="s-topbar--searchbar--input-group">
                                <input name="q"
                                       type="text"
                                       role="combobox"
                                       placeholder="Search&#x2026;"
                                       value=""
                                       autocomplete="off"
                                       maxlength="240"
                                       class="s-input s-input__search js-search-field "
                                       aria-label="Search"
                                       aria-controls="top-search" 
                                       data-controller="s-popover"
                                       data-action="focus->s-popover#show"
                                       data-s-popover-placement="bottom-start" />
                                <svg aria-hidden="true" class="s-input-icon s-input-icon__search svg-icon iconSearch" width="18" height="18"  viewBox="0 0 18 18"><path  d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18l1.5-1.5ZM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0Z"/></svg>
                                <div class="s-popover p0 wmx100 wmn4 sm:wmn-initial js-top-search-popover" id="top-search" role="menu">
        <div class="s-popover--arrow"></div>
        <div class="js-spinner p24 d-flex ai-center jc-center d-none">
            <div class="s-spinner s-spinner__sm fc-orange-400">
                <div class="v-visible-sr">Loading&#x2026;</div>
            </div>
        </div>
    
        <span class="v-visible-sr js-screen-reader-info"></span>
        <div class="js-ac-results overflow-y-auto hmx3 d-none"></div>
    
        <div class="js-search-hints" aria-describedby="Tips for searching"></div>
    </div>
                            </div>
                    </form>
            
    
    <nav class="h100 ml-auto overflow-x-auto pr12">
        <ol class="s-topbar--content" role="menubar">
        
        
        
            <li class="js-topbar-dialog-corral" role="presentation">
                    
    
        <div class="topbar-dialog siteSwitcher-dialog dno" role="menu">
            <div class="header fw-wrap">
                <h3 class="flex--item">
                    <a href="https://stackoverflow.com">current community</a>
                </h3>
                <div class="flex--item fl1">
                    <div class="ai-center d-flex jc-end">
                        <button
                            class="js-close-button s-btn s-btn__muted p0 ml8 d-none sm:d-block"
                            type="button"
                            aria-label="Close"
                        >
                            <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18"  viewBox="0 0 18 18"><path  d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9 15 4.41Z"/></svg>
                        </button>
                    </div>
                </div>
            </div>
            <div class="modal-content bg-blue-200 current-site-container">
                <ul class="current-site">
                        <li class="d-flex">
                                <div class="fl1">
                    <a href="https://stackoverflow.com"  
           class="current-site-link d-flex gx8 site-link js-gps-track"
           data-id="1"
           data-gps-track="site_switcher.click({ item_type:3 })">
            <div class="favicon favicon-stackoverflow site-icon flex--item" title="Stack Overflow"></div>
            <span class="flex--item fl1">
                Stack Overflow
            </span>
        </a>
    
        </div>
        <div class="related-links">
                <a href="https://stackoverflow.com/help" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:14 })">help</a>
                <a href="https://chat.stackoverflow.com/?tab=site&amp;host=stackoverflow.com" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:6 })">chat</a>
        </div>
    
                        </li>
                        <li class="related-site d-flex">
                                <div class="L-shaped-icon-container">
            <span class="L-shaped-icon"></span>
        </div>
    
                                <a href="https://meta.stackoverflow.com"  
           class="s-block-link px16 d-flex gx8 site-link js-gps-track"
           data-id="552"
           data-gps-track="site.switch({ target_site:552, item_type:3 }),site_switcher.click({ item_type:4 })">
            <div class="favicon favicon-stackoverflowmeta site-icon flex--item" title="Meta Stack Overflow"></div>
            <span class="flex--item fl1">
                Meta Stack Overflow
            </span>
        </a>
    
                        </li>
                </ul>
            </div>
    
            <div class="header" id="your-communities-header">
                <h3>
    your communities            </h3>
    
            </div>
            <div class="modal-content" id="your-communities-section">
    
                    <div class="call-to-login">
    <a href="https://stackoverflow.com/users/signup?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f64159777%2fstateful-lstm-tensorflow-invalid-input-h-shape-error" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:10 })">Sign up</a> or <a href="https://stackoverflow.com/users/login?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f64159777%2fstateful-lstm-tensorflow-invalid-input-h-shape-error" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:11 })">log in</a> to customize your list.                </div>
            </div>
    
            <div class="header">
                <h3><a href="https://stackexchange.com/sites">more stack exchange communities</a>
                </h3>
                <a href="https://stackoverflow.blog" class="float-right">company blog</a>
            </div>
            <div class="modal-content">
                    <div class="child-content"></div>
            </div>        
        </div>
    
            </li>
        
                <li role="none"><button class="s-topbar--item s-btn s-btn__icon s-btn__muted d-none sm:d-inline-flex js-searchbar-trigger" role="menuitem" aria-label="Search" aria-haspopup="true" aria-controls="search" title="Click to show search"><svg aria-hidden="true" class="svg-icon iconSearch" width="18" height="18"  viewBox="0 0 18 18"><path  d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18l1.5-1.5ZM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0Z"/></svg></button></li>
                            <li role="none">
                                <a href="https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f64159777%2fstateful-lstm-tensorflow-invalid-input-h-shape-error" class="s-topbar--item s-topbar--item__unset s-btn s-btn__outlined ws-nowrap js-gps-track" role="menuitem" rel="nofollow"
                   data-gps-track="login.click" data-ga="[&quot;top navigation&quot;,&quot;login button click&quot;,null,null,null]">Log in</a>
                            </li>
                                <li role="none"><a href="https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f64159777%2fstateful-lstm-tensorflow-invalid-input-h-shape-error" class="s-topbar--item s-topbar--item__unset ml4 s-btn s-btn__filled ws-nowrap js-signup-button js-gps-track" role="menuitem" rel="nofollow" data-gps-track="signup.topbar.click" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;Header&quot;,null,null]">Sign up</a></li>
        </ol>
    </nav>
    
    
        </div>
    </header>
    
        <script>
            StackExchange.ready(function () { StackExchange.topbar.init(); });
            StackExchange.scrollPadding.setPaddingTop(50, 10); 
        </script>
    
    
                    
    
    
        <div id="announcement-banner" class="js-announcement-banner bg-black-500 fc-white baw0 ff-sans fs-body2 py2"
             data-campaign="2024-05-14.overflowai-teams-launch" data-cookie="notice-oat" data-expire-date="1716868800000">
            <div class="d-flex jc-space-between wmx12 mx-auto px16 py8">
                <div class="flex--item mr12">
                    OverflowAI is here! AI power for your Stack Overflow for Teams knowledge community. <a target="_blank"
                       class="s-link s-link__underlined fc-white js-link js-gps-track fw-bold" href="https://stackoverflow.co/teams/ai/?utm_source=stackoverflow-community&amp;utm_medium=referral&amp;utm_campaign=teams-overflowai-launch&amp;utm_content=announcement-banner" data-ga="[&quot;overflowai-teams-launch&quot;,&quot;Announcement Banner&quot;,&quot;https://stackoverflow.co/teams/ai/?utm_source=stackoverflow-community&amp;utm_medium=referral&amp;utm_campaign=teams-overflowai-launch&amp;utm_content=announcement-banner&quot;,null,{&quot;dimension4&quot;:&quot;overflowai-teams-launch&quot;}]"
                       data-gps-track="announcement_banner.click({campaign: &#x27;2024-05-14.overflowai-teams-launch&#x27;, location: 2, action: 2})">Learn more</a>
                </div>
                <a class="flex--item fc-white js-dismiss js-gps-track" href="#" title="dismiss"
                   data-gps-track="announcement_banner.click({campaign: &#x27;2024-05-14.overflowai-teams-launch&#x27;, location: 2, action: 1})"><svg aria-hidden="true" class="m0 svg-icon iconClear" width="18" height="18"  viewBox="0 0 18 18"><path  d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9 15 4.41Z"/></svg></a>
            </div>
        </div>
        <script>
            StackExchange.ready(function () {
                StackExchange.Notice.announcementBannerInit();
            });
        </script>
    
    
                <div id="top-hero-div">
                        <div id="signup-dialog-container"></div>
    <script type="application/json" data-role="module-args" data-module-name="islands/signup-dialog/index.mod">{"ContainerElementId":"signup-dialog-container","FKey":"4a4af90770b3a1e583cccae29b6b66c55d0409a14103bc5d312f983c6775f325","VisitTimeout":30,"ReshowFrequency":3,"ReshowOffset":0,"InactiveTimeBeforeReshow":1.0,"OauthInPopup":false,"ReturnUrlForPopup":"https://stackoverflow.com/users/after-signup/oauth-only","Location":1,"IsSampleForHeroShowEvent":false,"ShowOnlyAfterEvent":true,"TriggerEvent":"one-tap-not-shown"}</script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/71.en.js?v=df900d976cca"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/8184.en.js?v=c565036a497f"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/5252.en.js?v=3e04489c620f"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/2931.en.js?v=627192fbc655"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/7940.en.js?v=ecf277db7e4a"></script><script defer src="https://cdn.sstatic.net/Js/islands/signup-dialog.en.js?v=72a708c1e6fc"></script>            </div>
    
    
        <div class="container">
                    
    
    
    <div id="left-sidebar" data-is-here-when="md lg" class="left-sidebar js-pinned-left-sidebar ps-relative">
        <div class="left-sidebar--sticky-container js-sticky-leftnav">
            <nav role="navigation">
                <ol class="nav-links">
                    <li>
                        <ol class="nav-links">
                            
    
    <li class="ps-relative"  aria-current="false">
    
    
        <a
           href="/"
           class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon"
           
           data-gps-track="top_nav.click({is_current: false, location:2, destination:8,  has_activity_notification:False});home_nav.click({location:2})"
           aria-controls=""
           data-controller=" "
           data-s-popover-placement="right"
           aria-current="false"
           data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
        >
            <div class="d-flex ai-center">
    <svg aria-hidden="true" class="svg-icon iconHome" width="18" height="18"  viewBox="0 0 18 18"><path  d="M15 10v5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-5H0l9-9 9 9h-3Zm-8 1v6h4v-6H7Z"/></svg>                <span class="-link--channel-name pl6">Home</span>
    
            </div>
        </a>
    </li>
    
    
    
                            
    
    <li class="ps-relative  youarehere"  aria-current="true">
    
    
        <a id="nav-questions"
           href="/questions"
           class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon"
           
           data-gps-track="top_nav.click({is_current: true, location:2, destination:1,  has_activity_notification:False})"
           aria-controls=""
           data-controller=" "
           data-s-popover-placement="right"
           aria-current="false"
           data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
        >
            <div class="d-flex ai-center">
    <svg aria-hidden="true" class="svg-icon iconQuestion" width="18" height="18"  viewBox="0 0 18 18"><path  d="m4 15-3 3V4c0-1.1.9-2 2-2h12c1.09 0 2 .91 2 2v9c0 1.09-.91 2-2 2H4Zm7.75-3.97c.72-.83.98-1.86.98-2.94 0-1.65-.7-3.22-2.3-3.83a4.41 4.41 0 0 0-3.02 0 3.8 3.8 0 0 0-2.32 3.83c0 1.29.35 2.29 1.03 3a3.8 3.8 0 0 0 2.85 1.07c.62 0 1.2-.11 1.71-.34.65.44 1 .68 1.06.7.23.13.46.23.7.3l.59-1.13a5.2 5.2 0 0 1-1.28-.66Zm-1.27-.9a5.4 5.4 0 0 0-1.5-.8l-.45.9c.33.12.66.29.98.5-.2.07-.42.11-.65.11-.61 0-1.12-.23-1.52-.68-.86-1-.86-3.12 0-4.11.8-.9 2.35-.9 3.15 0 .9 1.01.86 3.03-.01 4.08Z"/></svg>                <span class="-link--channel-name pl6">Questions</span>
    
            </div>
        </a>
    </li>
    
    
    
    
    
    
                            
    
    <li class="ps-relative"  aria-current="false">
    
    
        <a
           href="/tags"
           class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon"
           
           data-gps-track="top_nav.click({is_current: false, location:2, destination:2,  has_activity_notification:False})"
           aria-controls=""
           data-controller=" "
           data-s-popover-placement="right"
           aria-current="false"
           data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
        >
            <div class="d-flex ai-center">
    <svg aria-hidden="true" class="svg-icon iconTags" width="18" height="18"  viewBox="0 0 18 18"><path  d="M9.24 1a3 3 0 0 0-2.12.88l-5.7 5.7a2 2 0 0 0-.38 2.31 3 3 0 0 1 .67-1.01l6-6A3 3 0 0 1 9.83 2H14a3 3 0 0 1 .79.1A2 2 0 0 0 13 1H9.24Z" opacity=".4"/><path  d="M9.83 3a2 2 0 0 0-1.42.59l-6 6a2 2 0 0 0 0 2.82L6.6 16.6a2 2 0 0 0 2.82 0l6-6A2 2 0 0 0 16 9.17V5a2 2 0 0 0-2-2H9.83ZM12 9a2 2 0 1 1 0-4 2 2 0 0 1 0 4Z"/></svg>                <span class="-link--channel-name pl6">Tags</span>
    
            </div>
        </a>
    </li>
    
    
                            
                            <li class="pb24"></li>
    
    
                            
    
    <li class="ps-relative"  aria-current="false">
    
    
        <a id="nav-users"
           href="/users"
           class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon"
           
           data-gps-track="top_nav.click({is_current: false, location:2, destination:3,  has_activity_notification:False})"
           aria-controls=""
           data-controller=" "
           data-s-popover-placement="right"
           aria-current="false"
           data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
        >
            <div class="d-flex ai-center">
    <svg aria-hidden="true" class="svg-icon iconPeople" width="18" height="18"  viewBox="0 0 18 18"><path  d="M17 14c0 .44-.45 1-1 1H9a1 1 0 0 1-1-1H2c-.54 0-1-.56-1-1 0-2.63 3-4 3-4s.23-.4 0-1c-.84-.62-1.06-.59-1-3 .06-2.42 1.37-3 2.5-3s2.44.58 2.5 3c.06 2.41-.16 2.38-1 3-.23.59 0 1 0 1s1.55.71 2.42 2.09c.78-.72 1.58-1.1 1.58-1.1s.23-.4 0-1c-.84-.61-1.06-.58-1-3 .06-2.41 1.37-3 2.5-3s2.44.59 2.5 3c.05 2.42-.16 2.39-1 3-.23.6 0 1 0 1s3 1.38 3 4Z"/></svg>                <span class="-link--channel-name pl6">Users</span>
    
            </div>
        </a>
    </li>
    
    
                                
    
    <li class="ps-relative"  aria-current="false">
    
    
        <a id="nav-companies"
           href="https://stackoverflow.com/jobs/companies?so_medium=stackoverflow&amp;so_source=SiteNav"
           class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon"
           
           data-gps-track="top_nav.click({is_current: false, location:2, destination:12,  has_activity_notification:False})"
           aria-controls=""
           data-controller=" "
           data-s-popover-placement="right"
           aria-current="false"
           data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
        >
            <div class="d-flex ai-center">
    <svg aria-hidden="true" class="svg-icon iconIndustry" width="18" height="18"  viewBox="0 0 18 18"><path  d="M10 16v-4H8v4H2V4c0-1.1.9-2 2-2h6c1.09 0 2 .91 2 2v2h2c1.09 0 2 .91 2 2v8h-6ZM4 4v2h2V4H4Zm0 4v2h2V8H4Zm4-4v2h2V4H8Zm0 4v2h2V8H8Zm-4 4v2h2v-2H4Zm8 0v2h2v-2h-2Zm0-4v2h2V8h-2Z"/></svg>                <span class="-link--channel-name pl6">Companies</span>
    
            </div>
        </a>
    </li>
    
    
    
    
            <li class="ml8 mt32 mb8">
                <a href="javascript:void(0)"
                   class="s-link s-link d-flex fl-grow1 fc-black-400 h:fc-black-600 fs-fine"
                   role="button"
                   aria-controls="popover-labs-left-nav"
                   data-controller="s-popover"
                   data-action="s-popover#toggle"
                   data-s-popover-placement="top"
                   data-s-popover-toggle-class="is-selected"
                >
                    <div class="flex--item fl-grow1 tt-uppercase fc-black-600 fw-bold">Labs</div>
                    <div class="flex--item px12">
                        <svg aria-hidden="true" class="svg-icon iconInfoSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M7 1a6 6 0 1 1 0 12A6 6 0 0 1 7 1Zm1 10V6H6v5h2Zm0-6V3H6v2h2Z"/></svg>
                    </div>
                </a>
            </li>
            
    
    <li class="ps-relative"  aria-current="false">
    
    
        <a id="nav-labs-jobs"
           href="/jobs?source=so-left-nav"
           class="s-block-link pl8 ai-center js-disable-jobs-new-link js-gps-track nav-links--link -link__with-icon"
           
           data-gps-track="top_nav.click({is_current: false, location:2, destination:26,  has_activity_notification:False});jobs.click({destination:JobsFakeDoor, is_registered:False, rep_bucket:new, origin:Stack Overflow})"
           aria-controls=""
           data-controller=" "
           data-s-popover-placement="right"
           aria-current="false"
           data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
        >
            <div class="d-flex ai-center">
    <div class="d-flex ai-center mln8 mrn6 myn8 bg-purple-400 baw3 bas-solid bc-purple-200 bar-circle fc-white p4"><svg aria-hidden="true" class="fc-white bg-transparent svg-icon iconBriefcase" width="18" height="18"  viewBox="0 0 18 18"><path  d="M5 4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v1h1a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7c0-1.1.9-2 2-2h1V4Zm7 0H6v1h6V4Z"/></svg></div>                <span class="-link--channel-name pl6">Jobs</span>
    
                    <div class="ps-absolute flex--item r2 mx4 ml-auto">
                        <div class="s-badge s-badge__new s-badge__sm">New</div>
                    </div>
            </div>
        </a>
    </li>
    
    
                    
    
    <li class="ps-relative"  aria-current="false">
    
    
        <a id="nav-labs-discussions"
           href="/beta/discussions"
           class="s-block-link pl8 ai-center js-gps-track nav-links--link -link__with-icon"
           
           data-gps-track="top_nav.click({is_current: false, location:2, destination:24,  has_activity_notification:False})"
           aria-controls=""
           data-controller=" "
           data-s-popover-placement="right"
           aria-current="false"
           data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
        >
            <div class="d-flex ai-center">
    <svg aria-hidden="true" class="w16 svg-icon iconMessage" width="18" height="18"  viewBox="0 0 18 18"><path  d="M5 7a1 1 0 0 1 1-1h6a1 1 0 1 1 0 2H6a1 1 0 0 1-1-1Zm1 2a1 1 0 1 0 0 2h4a1 1 0 1 0 0-2H6Zm-5 9V4c0-1.1.9-2 2-2h12c1.09 0 2 .91 2 2v9c0 1.09-.91 2-2 2H4.5L1 18Zm2.76-5h11.23a.06.06 0 0 0 0-.01H15V4a.06.06 0 0 0-.01-.01H3v9.65l.76-.65Z"/></svg>                <span class="-link--channel-name pl6">Discussions</span>
    
            </div>
        </a>
    </li>
    
    
    
                                <li class="ml8 mt32 mb4">
                                    <div class="d-flex jc-space-between ai-center">
                                        <a
                                            class="s-link d-flex fl-grow1 fc-black-400 h:fc-black-600 fs-fine"
                                            href="javascript:void(0)"
                                            role="button"
                                            aria-controls="popover-discover-collectives"
                                            data-controller="s-popover"
                                            data-action="s-popover#toggle"
                                            data-s-popover-placement="top"
                                            data-s-popover-toggle-class="is-selected"
                                            data-gps-track="top_nav.click({is_current:false, location:2, destination:17})"
                                        >
                                            <div class="flex--item fl-grow1 tt-uppercase fc-black-600 fw-bold">Collectives</div>
                                            <div class="flex--item px12 js-collectives-navcta-toggle">
                                                <svg aria-hidden="true" class="svg-icon iconPlusSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M8 2H6v4H2v2h4v4h2V8h4V6H8V2Z"/></svg>
                                            </div>
                                        </a>
                                    </div>
    
                                </li>
                                    <li class="ps-relative js-collectives-navcta-toggle">
                                        <p class="fs-fine pr8 pl8 pt4 fc-black-400">
                                            Communities for your favorite technologies.  <a href="/collectives-all" class="s-link s-link__grayscale s-link__underlined fw-bold">Explore all Collectives</a>
                                        </p>
                                    </li>
    
                        </ol>
                    </li>
                    
                    
    
            
    
    <li class="js-freemium-cta ps-relative mt32 mb8">
    
    
        <div class="fs-fine tt-uppercase fc-black-600 fw-bold ml8 mt16 mb8">Teams</div>
    
        <div class="px12 pt12 pb4 mb12 fc-medium overflow-hidden">        
            <img class="wmx100 mx-auto mb12 h-auto d-block" width="151" height="24" src="https://cdn.sstatic.net/Img/teams/teams-promo.svg?v=e507948b81bf" alt="">
            <p class="fs-fine">
                Ask questions, find answers and collaborate at work with Stack Overflow for Teams.
            </p>
            <a href="https://stackoverflow.co/teams/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams" 
               class="w100 s-btn s-btn__filled s-btn__xs bg-orange-400 h:bg-orange-500 js-gps-track pt8 pr7 pb6 pl7"
               data-gps-track="teams.create.left-sidenav.click({ Action: 5 })"
               data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav free cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">Explore Teams</a>
            <a href="https://stackoverflowteams.com/teams/create/free/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams"
               class="w100 s-btn s-btn__muted s-btn__xs mt1 js-gps-track"
               data-gps-track="teams.create.left-sidenav.click({ Action: 6 })"
               data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav free cta&quot;,&quot;stackoverflow.com/teams/create/free&quot;,null,null]">Create a free Team</a>
        </div>
    </li>
    
    
        <li class="d-flex ai-center jc-space-between ml8 mt32 mb8 js-create-team-cta d-none">
    
            <a href="javascript:void(0)"
                class="s-link d-flex fl-grow1 fc-black-400 h:fc-black-600 fs-fine js-gps-track"
                role="button"
                aria-controls="popover-teams-create-cta"
                data-controller="s-popover"
                data-action="s-popover#toggle"
                data-s-popover-placement="bottom-start"
                data-s-popover-toggle-class="is-selected"
                data-gps-track="teams.create.left-sidenav.click({ Action: ShowInfo })"
                data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav show teams info&quot;,null,null,null]"
             >
                <div class="flex--item fl-grow1 fc-black-600 fw-bold tt-uppercase">Teams</div>
                <div class="flex--item px12">
                    <svg aria-hidden="true" class="svg-icon iconPlusSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M8 2H6v4H2v2h4v4h2V8h4V6H8V2Z"/></svg>
                </div>
            </a>
        </li>
        <li class="ps-relative js-create-team-cta d-none">
            <p class="fs-fine pr8 pl8 pb4 fc-black-400">
                Ask questions, find answers and collaborate at work with Stack Overflow for Teams.
                <a href="https://stackoverflow.co/teams/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams-compact" class="s-link s-link__grayscale s-link__underlined fw-bold">Explore Teams</a>
            </p>
        </li> 
    
                </ol>
            </nav>
        </div>
    
    
            <div class="s-popover ws2" id="popover-discover-collectives" role="menu">
                <div class="s-popover--arrow"></div>
                <div>
                    <svg aria-hidden="true" class="fc-orange-400 float-right ml24 svg-spot spotCollective" width="48" height="48"  viewBox="0 0 48 48"><path  d="M25.5 7a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5ZM14 18.25c0-.69.56-1.25 1.25-1.25h22.5c.69 0 1.25.56 1.25 1.25V37.5a1 1 0 0 1-1.6.8l-4.07-3.05a1.25 1.25 0 0 0-.75-.25H15.25c-.69 0-1.25-.56-1.25-1.25v-15.5ZM7 24.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0ZM25.5 48a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5ZM48 24.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0Z" opacity=".2"/><path  d="M21 3.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0ZM24.5 2a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3ZM0 23.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0ZM3.5 22a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3ZM21 44.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0Zm3.5-1.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Zm20-23a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7ZM43 23.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Zm-23.23-3.14a1 1 0 0 1-.13 1.4l-2.08 1.74 2.08 1.73a1 1 0 1 1-1.28 1.54l-2.42-2.02a1.63 1.63 0 0 1 0-2.5l2.42-2.02a1 1 0 0 1 1.4.13Zm7.59 1.41a1 1 0 1 1 1.28-1.54l2.42 2.02c.78.65.78 1.85 0 2.5l-2.42 2.02a1 1 0 1 1-1.28-1.54l2.08-1.73-2.08-1.73ZM24.12 18a1 1 0 0 1 .87 1.12l-1 8a1 1 0 1 1-1.98-.24l1-8a1 1 0 0 1 1.11-.87Zm-11.87-5C11.01 13 10 14 10 15.25v15.5c0 1.24 1 2.25 2.25 2.25h17.33c.06 0 .11.02.15.05l4.07 3.05a2 2 0 0 0 3.2-1.6V15.25c0-1.24-1-2.25-2.25-2.25h-22.5ZM12 15.25c0-.14.11-.25.25-.25h22.5c.14 0 .25.11.25.25V34.5l-4.07-3.05a2.2 2.2 0 0 0-1.35-.45H12.25a.25.25 0 0 1-.25-.25v-15.5Zm7.24-10.68a1 1 0 1 0-.48-1.94A22.04 22.04 0 0 0 2.91 17.7a1 1 0 1 0 1.92.58 20.04 20.04 0 0 1 14.4-13.72Zm11.05-1.66a1 1 0 0 0-.58 1.92c6.45 1.92 11.54 7 13.46 13.46a1 1 0 1 0 1.92-.58 22.05 22.05 0 0 0-14.8-14.8ZM4.57 28.76a1 1 0 0 0-1.94.48 22.03 22.03 0 0 0 16.13 16.13 1 1 0 1 0 .48-1.94A20.03 20.03 0 0 1 4.57 28.76Zm40.8.48a1 1 0 1 0-1.94-.48 20.04 20.04 0 0 1-13.72 14.41 1 1 0 0 0 .58 1.92 22.04 22.04 0 0 0 15.08-15.85Z"/></svg>
                    <h5 class="pt4 fw-bold">Collectives™ on Stack Overflow</h5>
                    <p class="my16 fs-caption fc-black-500">Find centralized, trusted content and collaborate around the technologies you use most.</p>
                    <a href="/collectives"
                class="js-gps-track s-btn s-btn__filled s-btn__xs"
                data-gps-track="top_nav.click({is_current:false, location:2, destination:18})">
                        Learn more about Collectives
                    </a>
                </div>
            </div>
    
            <div class="s-popover ws2"
            id="popover-teams-create-cta"
            role="menu"
            aria-hidden="true">
                <div class="s-popover--arrow"></div>
    
                <div class="ps-relative overflow-hidden">
                    <p class="mb2"><strong>Teams</strong></p>
                    <p class="mb12 fs-caption fc-black-400">Q&amp;A for work</p>
                    <p class="mb12 fs-caption fc-black-500">Connect and share knowledge within a single location that is structured and easy to search.</p>
                    <a href="https://stackoverflow.co/teams/"
                class="js-gps-track s-btn s-btn__filled s-btn__xs"
                data-gps-track="teams.create.left-sidenav.click({ Action: CtaClick })"
                data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">
                        Learn more about Teams
                    </a>
                </div>
    
                <div class="ps-absolute t8 r8">
                    <svg aria-hidden="true" class="fc-orange-400 svg-spot spotPeople" width="48" height="48"  viewBox="0 0 48 48"><path  d="M13.5 28a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM7 30a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v5h11v-5a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v10a2 2 0 0 1-2 2H33v5a1 1 0 0 1-1 1H20a1 1 0 0 1-1-1v-5H8a1 1 0 0 1-1-1V30Zm25-6.5a4.5 4.5 0 1 0 9 0 4.5 4.5 0 0 0-9 0ZM24.5 34a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9Z" opacity=".2"/><path  d="M16.4 26.08A6 6 0 1 0 7.53 26C5.64 26.06 4 27.52 4 29.45V40a1 1 0 0 0 1 1h9a1 1 0 1 0 0-2h-4v-7a1 1 0 1 0-2 0v7H6v-9.55c0-.73.67-1.45 1.64-1.45H16a1 1 0 0 0 .4-1.92ZM12 18a4 4 0 1 1 0 8 4 4 0 0 1 0-8Zm16.47 14a6 6 0 1 0-8.94 0A3.6 3.6 0 0 0 16 35.5V46a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V35.5c0-1.94-1.64-3.42-3.53-3.5ZM20 28a4 4 0 1 1 8 0 4 4 0 0 1-8 0Zm-.3 6h8.6c1 0 1.7.75 1.7 1.5V45h-2v-7a1 1 0 1 0-2 0v7h-4v-7a1 1 0 1 0-2 0v7h-2v-9.5c0-.75.7-1.5 1.7-1.5ZM42 22c0 1.54-.58 2.94-1.53 4A3.5 3.5 0 0 1 44 29.45V40a1 1 0 0 1-1 1h-9a1 1 0 1 1 0-2h4v-7a1 1 0 1 1 2 0v7h2v-9.55A1.5 1.5 0 0 0 40.48 28H32a1 1 0 0 1-.4-1.92A6 6 0 1 1 42 22Zm-2 0a4 4 0 1 0-8 0 4 4 0 0 0 8 0Z"/><g  opacity=".35"><path d="M17 10a1 1 0 011-1h12a1 1 0 110 2H18a1 1 0 01-1-1Zm1-5a1 1 0 100 2h12a1 1 0 100-2H18ZM14 1a1 1 0 00-1 1v12a1 1 0 001 1h5.09l4.2 4.2a1 1 0 001.46-.04l3.7-4.16H34a1 1 0 001-1V2a1 1 0 00-1-1H14Zm1 12V3h18v10h-5a1 1 0 00-.75.34l-3.3 3.7-3.74-3.75a1 1 0 00-.71-.29H15Z"/></g></svg>
                </div>
            </div>
    
            <div class="s-popover ws2"
                 id="popover-labs-left-nav"
                 role="menu"
                 aria-hidden="true">
                <div class="s-popover--arrow"></div>
                <svg aria-hidden="true" class="fc-black-600 mb8 svg-icon iconLabs" width="42" height="18"><path d="M11.5 13.624a.374.374 0 0 1-.37.376H5.361a.374.374 0 0 1-.37-.376V4.376c0-.207.165-.376.37-.376H6.62c.204 0 .37.169.37.376v7.611h4.138c.205 0 .371.169.371.377v1.26zm9.432.215c-.07.1-.185.161-.308.161H19.13a.376.376 0 0 1-.356-.254l-.55-1.7h-3.111l-.55 1.7a.377.377 0 0 1-.355.254h-1.494a.376.376 0 0 1-.353-.506l3.39-9.247A.376.376 0 0 1 16.103 4h1.13c.158 0 .299.099.353.247l3.39 9.247a.376.376 0 0 1-.045.345zm-4.157-7.386l-1.219 3.531h2.266l-1.047-3.53zm13.335 5.71a.37.37 0 0 0-.003.524c.956.971 2.047 1.313 3.486 1.313 1.014 0 1.92-.265 2.582-.788.67-.53 1.063-1.306 1.063-2.255 0-.855-.268-1.622-.867-2.145-.456-.41-1.008-.633-1.89-.767l-1.037-.153c-.377-.057-.672-.19-.832-.332-.146-.132-.221-.315-.221-.568 0-.309.11-.56.306-.737.199-.179.518-.312.986-.312.708 0 1.254.151 1.726.601a.37.37 0 0 0 .516-.004l.883-.87a.37.37 0 0 0-.008-.534C35.942 4.334 35.004 4 33.721 4c-1.016 0-1.872.292-2.479.836-.61.548-.935 1.32-.935 2.207 0 .82.243 1.502.781 2.01h.001c.468.437 1.135.716 1.93.826l1.072.153c.508.073.647.147.795.286l.008.007c.14.125.234.34.234.67 0 .332-.124.567-.344.73-.235.174-.617.293-1.165.293-.867 0-1.49-.185-2.066-.76a.37.37 0 0 0-.522-.003l-.92.908zM22.37 14a.374.374 0 0 1-.37-.376V4.376c0-.207.166-.376.37-.376h3.543c.913 0 1.697.264 2.257.78.564.519.863 1.259.863 2.129 0 .845-.377 1.524-.87 1.947.57.433 1.01 1.145 1.01 2.157 0 .941-.317 1.702-.894 2.224-.57.517-1.354.763-2.225.763H22.37zm3.543-1.977c.96 0 .959-1.01.959-1.01s0-1.013-.959-1.013H24v2.023h1.913zm-.115-4.063c1.074 0 1.074-1.015 1.074-1.015s0-1.016-1.074-1.016H24V7.96h1.798z" fill="var(--black-600)"/><path d="M0 4v10a4 4 0 0 0 4 4h34a4 4 0 0 0 4-4V4a4 4 0 0 0-4-4H4a4 4 0 0 0-4 4zm4-2h34a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z" fill="var(--black-600)"/></svg>
                <p class="fs-caption">Get early access and see previews of new features.</p>
                <a class="s-btn s-btn__filled s-btn__xs s-btn__icon fs-fine" href="https://stackoverflow.co/labs/"><svg aria-hidden="true" class="svg-icon iconShareSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M5 1H3a2 2 0 0 0-2 2v8c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V9h-2v2H3V3h2V1Zm2 0h6v6h-2V4.5L6.5 9 5 7.5 9.5 3H7V1Z"/></svg> Learn more about Labs</a>
            </div>
    
    
    
    </div>
    
    
    
            <div id="content" class="snippet-hidden">
    
                
    
    <div itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
        <link itemprop="image" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
    
        <div class="inner-content clearfix">
            
    
                <div id="question-header" class="d-flex sm:fd-column">
                            <h1 itemprop="name" class="fs-headline1 ow-break-word mb8 flex--item fl1"><a href="/questions/64159777/stateful-lstm-tensorflow-invalid-input-h-shape-error" class="question-hyperlink">Stateful LSTM Tensorflow Invalid Input_h Shape Error</a></h1>
    
                    <div class="ml12 aside-cta flex--item sm:ml0 sm:mb12 sm:order-first d-flex jc-end">
    
                            <div class="ml12 aside-cta flex--item print:d-none">
                                    <a href="/questions/ask" class="ws-nowrap s-btn s-btn__filled">
            Ask Question
        </a>
    
                            </div>
                    </div>
                </div>
                <div class="d-flex fw-wrap pb8 mb16 bb bc-black-200">
                        <div class="flex--item ws-nowrap mr16 mb8" title="2020-10-01 16:40:51Z">
                            <span class="fc-black-400 mr2">Asked</span>
                            <time itemprop="dateCreated" datetime="2020-10-01T16:40:51">3 years, 7 months ago</time>
                        </div>
                        <div class="flex--item ws-nowrap mr16 mb8">
                            <span class="fc-black-400 mr2">Modified</span>
                            <a href="?lastactivity" class="s-link s-link__inherit" title="2020-10-20 19:11:42Z">3 years, 6 months ago</a>
                        </div>
                        <div class="flex--item ws-nowrap mb8" title="Viewed 2,998 times">
                            <span class="fc-black-400 mr2">Viewed</span>
                            3k times
                        </div>
                </div>
    
                <div id="mainbar" role="main" aria-label="question and answers">
                    
    <script defer src="https://cdn.sstatic.net/Js/webpack-chunks/71.en.js?v=df900d976cca"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/8184.en.js?v=c565036a497f"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/6828.en.js?v=4c50b1e12ff1"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/770.en.js?v=a7642057f09d"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/8995.en.js?v=5c516205f55e"></script><script defer src="https://cdn.sstatic.net/Js/islands/voting-prompt.en.js?v=4fa42a96b018"></script>
    
    <div class="question js-question" data-questionid="64159777" data-position-on-page="0" data-score="3"  id="question">
        <style>
        </style>
    <div class="js-zone-container zone-container-main">
        <div id="dfp-tlb" class="everyonelovesstackoverflow everyoneloves__top-leaderboard everyoneloves__leaderboard"></div>
            <div class="js-report-ad-button-container " style="width: 728px"></div>
    </div>
    
    
        <div class="post-layout ">
            <div class="votecell post-layout--left">
                
    
    
    <div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="64159777" data-referrer="None">
            <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200"
                    data-controller="s-tooltip"
                    data-s-tooltip-placement="right"
                    title="This question shows research effort; it is useful and clear"
                    aria-pressed="false"
                    aria-label="Up vote"
                    data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100"
                    data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
                <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18"  viewBox="0 0 18 18"><path  d="M1 12h16L9 4l-8 8Z"/></svg>
            </button>
            <input type="hidden" id="voteUpHash" value="70:3:31e,16:aa693533e0b3874a,10:1715767546,16:f511a56aee85c64b,8:64159777,0b0ad176b0f6e764c445683ed3bbc438a802cf3325062cd006499360e106aea8" />
            <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4"
                 itemprop="upvoteCount"
                 data-value="3">
                3
            </div>
            <button
                    class="js-vote-down-btn js-vote-down-question flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200"
                    title="This question does not show any research effort; it is unclear or not useful"
                    aria-pressed="false"
                    aria-label="Down vote"
                    data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100"
                    data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
                <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18"  viewBox="0 0 18 18"><path  d="M1 6h16l-8 8-8-8Z"/></svg>
            </button>
            <input type="hidden" id="voteDownHash" value="70:3:31e,16:baf2cf1bc0d63336,10:1715767546,16:ca0890962334c4f3,8:64159777,a8f52ae992296d11f1529c73e274bd1ae903c13490b3c04dd004f55d55bac169" />
    
    
            
    <button class="js-saves-btn s-btn s-btn__unset c-pointer py4"
            type="button"
            id="saves-btn-64159777"
            data-controller="s-tooltip"
            data-s-tooltip-placement="right"
            data-s-popover-placement=""
            title="Save this question."
            aria-pressed="false"
            data-post-id="64159777"
            data-post-type-id="1"
            data-user-privilege-for-post-click="0"
            aria-controls=""
            data-s-popover-auto-show="false"
    >
        <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18"  viewBox="0 0 18 18"><path  d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"/></svg>
        <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18"  viewBox="0 0 18 18"><path  d="m9 10.6 4 2.66V3H5v10.26l4-2.66ZM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"/></svg>
    </button>
    
    
    
    
    
    
    
    
        
        <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/64159777/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" title="Show activity on this post." aria-label="Timeline"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18"  viewBox="0 0 19 18"><path  d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4h3L3 9Zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5Z"/></svg></a>
    
    </div>
    
            </div>
    
            
    
    <div class="postcell post-layout--right">
        
        <div class="s-prose js-post-body" itemprop="text">
                    
    <p>I am experimenting with stateful LSTM on a time-series regression problem by using TensorFlow. I apologize that I cannot share the dataset.
    Below is my code.</p>
    <pre><code>train_feature = train_feature.reshape((train_feature.shape[0], 1, train_feature.shape[1]))
    val_feature = val_feature.reshape((val_feature.shape[0], 1, val_feature.shape[1]))
    
    batch_size = 64
    
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.LSTM(50, batch_input_shape=(batch_size, train_feature.shape[1], train_feature.shape[2]), stateful=True))
    model.add(tf.keras.layers.Dense(1))
    
    model.compile(optimizer='adam',
                  loss='mse',
                  metrics=[tf.keras.metrics.RootMeanSquaredError()])
    
    model.fit(train_feature, train_label, 
              epochs=10,
              batch_size=batch_size)
    </code></pre>
    <p>When I run the above code, after the end of the first epoch, I will get an error as follows.</p>
    <pre><code>InvalidArgumentError:  [_Derived_]  Invalid input_h shape: [1,64,50] [1,49,50]
         [[{{node CudnnRNN}}]]
         [[sequential_1/lstm_1/StatefulPartitionedCall]] [Op:__inference_train_function_1152847]
    
    Function call stack:
    train_function -&gt; train_function -&gt; train_function
    </code></pre>
    <p>However, the model will be successfully trained if I change the <strong>batch_size to 1</strong>, and change the code for model training to the following.</p>
    <pre><code>total_epochs = 10
    
    for i in range(total_epochs):
        model.fit(train_feature, train_label, 
                  epochs=1,
                  validation_data=(val_feature, val_label),
                  batch_size=batch_size,
                  shuffle=False)
    
        model.reset_states()
    </code></pre>
    <p>Nevertheless, with a very large data (1 million rows), the model training will take a very long time since the batch_size is 1.</p>
    <p>So, I wonder, how to train a stateful LSTM with a batch size larger than 1 (e.g. 64), without getting the invalid input_h shape error?</p>
    <p>Thanks for your answers.</p>
        </div>
    
            <div class="mt24 mb12">
                <div class="post-taglist d-flex gs4 gsy fd-column">
                    <div class="d-flex ps-relative fw-wrap">
                        
                        <ul class='ml0 list-ls-none js-post-tag-list-wrapper d-inline'><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/tensorflow" class="post-tag" title="show questions tagged &#39;tensorflow&#39;" aria-label="show questions tagged &#39;tensorflow&#39;" rel="tag" aria-labelledby="tag-tensorflow-tooltip-container" data-tag-menu-origin="Unknown">tensorflow</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/keras" class="post-tag" title="show questions tagged &#39;keras&#39;" aria-label="show questions tagged &#39;keras&#39;" rel="tag" aria-labelledby="tag-keras-tooltip-container" data-tag-menu-origin="Unknown">keras</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/neural-network" class="post-tag" title="show questions tagged &#39;neural-network&#39;" aria-label="show questions tagged &#39;neural-network&#39;" rel="tag" aria-labelledby="tag-neural-network-tooltip-container" data-tag-menu-origin="Unknown">neural-network</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/lstm" class="post-tag" title="show questions tagged &#39;lstm&#39;" aria-label="show questions tagged &#39;lstm&#39;" rel="tag" aria-labelledby="tag-lstm-tooltip-container" data-tag-menu-origin="Unknown">lstm</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/lstm-stateful" class="post-tag" title="show questions tagged &#39;lstm-stateful&#39;" aria-label="show questions tagged &#39;lstm-stateful&#39;" rel="tag" aria-labelledby="tag-lstm-stateful-tooltip-container" data-tag-menu-origin="Unknown">lstm-stateful</a></li></ul>
                    </div>
                </div>
            </div>
    
        <div class="mb0 ">
            <div class="mt16 d-flex gs8 gsy fw-wrap jc-end ai-start pt4 mb16">
                <div class="flex--item mr16 fl1 w96">
                    
    
    
    <div class="js-post-menu pt2" data-post-id="64159777" data-post-type-id="1">
    
        <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">
    
            <div class="flex--item">
                <a href="/q/64159777"
                   rel="nofollow"
                   itemprop="url"
                   class="js-share-link js-gps-track"
                   title="Short permalink to this question"
                   data-gps-track="post.click({ item: 2, priv: 0, post_type: 1 })"
                   data-controller="se-share-sheet"
                   data-se-share-sheet-title="Share a link to this question"
                   data-se-share-sheet-subtitle=""
                   data-se-share-sheet-post-type="question"
                   data-se-share-sheet-social="facebook twitter devto"
                   data-se-share-sheet-location="1"
                   data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f4.0%2f"
                   data-se-share-sheet-license-name="CC BY-SA 4.0"
                   data-s-popover-placement="bottom-start">Share</a>
            </div>
    
    
    
                    <div class="flex--item">
                        <button type="button"
                                id="btnFollowPost-64159777" class="s-btn s-btn__link js-follow-post js-follow-question js-gps-track"
                                data-gps-track="post.click({ item: 14, priv: 0, post_type: 1 })"
                                data-controller="s-tooltip " data-s-tooltip-placement="bottom"
                                data-s-popover-placement="bottom" aria-controls=""
                                title="Follow this question to receive notifications">
                            Follow
                            <input type="hidden" id="voteFollowHash" value="70:3:31e,16:8a0fc81d258a6980,10:1715767546,16:a7677b479c976b9f,8:64159777,577985e35f3ad6585b0c8ca47250cd9f54052cd204caffc820311839d4bed33a" />
                        </button>
                    </div>
    
    
    
    
    
    
        </div>
        <div class="js-menu-popup-container"></div>
    </div>
                </div>
    
                <div class="post-signature owner flex--item">
                    <div class="user-info ">
        <div class="d-flex ">
            <div class="user-action-time fl-grow1">
                asked <span title='2020-10-01 16:40:51Z' class='relativetime'>Oct 1, 2020 at 16:40</span>
            </div>
            
        </div>
        <div class="user-gravatar32">
            <a href="/users/14055413/glorian"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/36fc836a9b091cc2f65fb70fabdf1200?s=64&amp;d=identicon&amp;r=PG&amp;f=y&amp;so-version=2" alt="glorian&#39;s user avatar" width="32" height="32" class="bar-sm"></div></a>
        </div>
        <div class="user-details" itemprop="author" itemscope itemtype="http://schema.org/Person">
            <a href="/users/14055413/glorian">glorian</a><span class="d-none" itemprop="name">glorian</span>
            <div class="-flair">
                <span class="reputation-score" title="reputation score " dir="ltr">53</span><span title="1 silver badge" aria-hidden="true"><span class="badge2"></span><span class="badgecount">1</span></span><span class="v-visible-sr">1 silver badge</span><span title="6 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">6</span></span><span class="v-visible-sr">6 bronze badges</span>
            </div>
        </div>
    </div>
    
    
                </div>
            </div>
        </div>
        
    </div>
    
    
    
    
                <span class="d-none" itemprop="commentCount">1</span> 
        <div class="post-layout--right js-post-comments-component">
            <div id="comments-64159777" class="comments js-comments-container bt bc-black-200 mt12 " data-post-id="64159777" data-min-length="15">
                <ul class="comments-list js-comments-list"
                        data-remaining-comments-count="0"
                        data-canpost="false"
                        data-cansee="true"
                        data-comments-unavailable="false"
                        data-addlink-disabled="true">
    
                            <li id="comment-113966647" class="comment js-comment " data-comment-id="113966647" data-comment-owner-id="9808917" data-comment-score="0">
            <div class="js-comment-actions comment-actions">
                <div class="comment-score js-comment-score js-comment-edit-hide">
                </div>
            </div>
            <div class="comment-text  js-comment-text-and-form">
                <div class="comment-body js-comment-edit-hide">
                    
                    <span class="comment-copy">I updated my answer for clarity. It now uses the example code you provided in the question. I think that would be helpful for others that may have this same question in the future. Cheers.</span>
                    
                    <div class="d-inline-flex ai-center">
    &ndash;&nbsp;<a href="/users/9808917/princy"
                                    title="343 reputation"
                                    class="comment-user">Princy</a>
                    </div>
                    <span class="comment-date" dir="ltr"><span title='2020-10-20 18:58:43Z, License: CC BY-SA 4.0' class='relativetime-clean'>Oct 20, 2020 at 18:58</span></span>
                </div>
            </div>
        </li>
    
                </ul>
            </div>
    
            <div id="comments-link-64159777" data-rep=50 data-anon=true>
                        <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid answering questions in comments."  href="#" role="button">Add a comment</a>
                    <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
                <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href=# onclick="" role="button"></a>
            </div>         
        </div>
        </div>
    
    </div>
    
    
    <div class="js-zone-container zone-container-responsive">
        <div id="dfp-isb" class="everyonelovesstackoverflow everyoneloves__inline-sidebar mx-auto"></div>
            <div class="js-report-ad-button-container mx-auto" style="width: 300px"></div>
    </div>
    
                    
                    
                    <div id="answers">
                        <a name="tab-top"></a>
                        <div id="answers-header">
                            <div class="answers-subheader d-flex ai-center mb8">
                                <div class="flex--item fl1">
                                    <h2 class="mb0" data-answercount="1">
                                            1 Answer
                                        <span style="display:none;" itemprop="answerCount">1</span>
                                    </h2>
                                </div>
                                <div class="flex--item">
                                    
    
    <div class="d-flex g4 gsx ai-center sm:fd-column sm:ai-start">
        <div class="d-flex fd-column ai-end sm:ai-start">
            <label class="flex--item fs-caption" for="answer-sort-dropdown-select-menu">
                Sorted by:
            </label>
            <a 
                class="js-sort-preference-change s-link flex--item fs-fine d-none"
                data-value="ScoreDesc"
                href="/questions/64159777/stateful-lstm-tensorflow-invalid-input-h-shape-error?answertab=scoredesc#tab-top"
            >
                Reset to default
            </a>
        </div>
        <div class="flex--item s-select">
            <select id="answer-sort-dropdown-select-menu">
                        <option
                            value=scoredesc
                            selected=selected
                        >
                            Highest score (default)
                        </option>
                        <option
                            value=trending
                        >
                            Trending (recent votes count more)
                        </option>
                        <option
                            value=modifieddesc
                        >
                            Date modified (newest first)
                        </option>
                        <option
                            value=createdasc
                        >
                            Date created (oldest first)
                        </option>
            </select>
        </div>
    </div>
    
    
                                </div>
                            </div>
                                
                        </div>
    
    
                                        
    <a name="64436749"></a>
    <div id="answer-64436749" class="answer js-answer" data-answerid="64436749" data-parentid="64159777" data-score="9" data-position-on-page="1" data-highest-scored="1" data-question-has-accepted-highest-score="0"  itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
        <div class="post-layout">
            <div class="votecell post-layout--left">
                
    
    
    <div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="64436749" data-referrer="None">
            <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200"
                    data-controller="s-tooltip"
                    data-s-tooltip-placement="right"
                    title="This answer is useful"
                    aria-pressed="false"
                    aria-label="Up vote"
                    data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100"
                    data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
                <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18"  viewBox="0 0 18 18"><path  d="M1 12h16L9 4l-8 8Z"/></svg>
            </button>
            <input type="hidden" id="voteUpHash" value="70:3:31e,16:57f8851e7cf830cf,10:1715767546,16:4b5040dad981fc19,8:64436749,5e0b691537fafed2340512b863ab233be8421325a2cf74bf25c8c829c0b50e5b" />
            <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4"
                 itemprop="upvoteCount"
                 data-value="9">
                9
            </div>
            <button
                    class="js-vote-down-btn flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200"
                    title="This answer is not useful"
                    aria-pressed="false"
                    aria-label="Down vote"
                    data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100"
                    data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
                <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18"  viewBox="0 0 18 18"><path  d="M1 6h16l-8 8-8-8Z"/></svg>
            </button>
            <input type="hidden" id="voteDownHash" value="70:3:31e,16:66bf4543ca8fe563,10:1715767546,16:118a313dad3a2308,8:64436749,670c19e2c74f0a9707d9e33f3f8610913874445779d5c393fafad844e70cb8c5" />
    
    
            
    <button class="js-saves-btn s-btn s-btn__unset c-pointer py4"
            type="button"
            id="saves-btn-64436749"
            data-controller="s-tooltip"
            data-s-tooltip-placement="right"
            data-s-popover-placement=""
            title="Save this answer."
            aria-pressed="false"
            data-post-id="64436749"
            data-post-type-id="2"
            data-user-privilege-for-post-click="0"
            aria-controls=""
            data-s-popover-auto-show="false"
    >
        <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18"  viewBox="0 0 18 18"><path  d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"/></svg>
        <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18"  viewBox="0 0 18 18"><path  d="m9 10.6 4 2.66V3H5v10.26l4-2.66ZM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"/></svg>
    </button>
    
    
    
    
    
    
    
                <div class="js-accepted-answer-indicator flex--item fc-green-400 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted&#x2026;" tabindex="0" role="note" aria-label="Accepted">
                    <div class="ta-center">
                        <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36"  viewBox="0 0 36 36"><path  d="m6 14 8 8L30 6v8L14 30l-8-8v-8Z"/></svg>
                    </div>
                </div>
    
        
        <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/64436749/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" title="Show activity on this post." aria-label="Timeline"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18"  viewBox="0 0 19 18"><path  d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4h3L3 9Zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5Z"/></svg></a>
    
    </div>
    
            </div>
    
            
    
    <div class="answercell post-layout--right">
        
        <div class="s-prose js-post-body" itemprop="text">
    <p>The fix is to <strong>ensure batch size never changes between batches</strong>. They must all be the same size.</p>
    <h2>Method 1</h2>
    <p>One way is to use a <strong>batch size that perfectly divides your dataset into equal-sized batches</strong>. For example, if total size of data is 1500 examples, then use a batch size of 50 or 100 or some other proper divisor of 1500.</p>
    <pre><code>batch_size = len(data)/proper_divisor
    </code></pre>
    <h2>Method 2</h2>
    <p>The other way is to <strong>ignore any batch that is less than the specified size</strong>, and this can be  done using the TensorFlow Dataset API and setting the <code>drop_remainder</code> to <code>True</code>.</p>
    <pre><code>batch_size = 64
    
    train_data = tf.data.Dataset.from_tensor_slices((train_feature, train_label))
    
    train_data = train_data.repeat().batch(batch_size, drop_remainder=True)
    
    steps_per_epoch = len(train_feature) // batch_size 
    
    model.fit(train_data, 
              epochs=10, steps_per_epoch = steps_per_epoch)
    
    </code></pre>
    <p>When using the Dataset API like above, you will need to also specify how many rounds of training count as an epoch (essentially how many batches to count as 1 epoch). A <code>tf.data.Dataset</code> instance (the result from <code>tf.data.Dataset.from_tensor_slices</code>) doesn't know the size of the data that it's streaming to the model, so what constitutes as one epoch has to be manually specified with <code>steps_per_epoch</code>.</p>
    <p>Your new code will look like this:</p>
    <pre><code>train_feature = train_feature.reshape((train_feature.shape[0], 1, train_feature.shape[1]))
    val_feature = val_feature.reshape((val_feature.shape[0], 1, val_feature.shape[1]))
    
    batch_size = 64
    train_data = tf.data.Dataset.from_tensor_slices((train_feature, train_label))
    train_data = train_data.repeat().batch(batch_size, drop_remainder=True)
    
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.LSTM(50, batch_input_shape=(batch_size, train_feature.shape[1], train_feature.shape[2]), stateful=True))
    model.add(tf.keras.layers.Dense(1))
    
    model.compile(optimizer='adam',
                  loss='mse',
                  metrics=[tf.keras.metrics.RootMeanSquaredError()])
    
    steps_per_epoch = len(train_feature) // batch_size 
    model.fit(train_data, 
              epochs=10, steps_per_epoch = steps_per_epoch)
    </code></pre>
    <p>You can also include the validation set as well, like this (not showing other code):</p>
    <pre><code>
    batch_size = 64
    val_data = tf.data.Dataset.from_tensor_slices((val_feature, val_label))
    val_data = val_data.repeat().batch(batch_size, drop_remainder=True)
    
    validation_steps = len(val_feature) // batch_size 
    model.fit(train_data, epochs=10, 
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps)
    
    </code></pre>
    <p><strong>Caveat:</strong> This means a few datapoints will never be seen by the model. To get around that, you can shuffle the dataset each round of training, so that the datapoints left behind each epoch changes, giving everyone a chance to be seen by the model.</p>
    <pre><code>buffer_size = 1000 # the bigger the slower but more effective shuffling.
    
    train_data = tf.data.Dataset.from_tensor_slices((train_feature, train_label))
    train_data = train_data.shuffle(buffer_size=buffer_size, reshuffle_each_iteration=True)
    train_data = train_data.repeat().batch(batch_size, drop_remainder=True)
    
    </code></pre>
    <h2>Why the error occurs</h2>
    <p>Stateful RNNs and their variants (LSTM, GRU, etc.) require fixed batch size. The reason is simply because statefulness is one way to realize Truncated Backprop Through Time, by passing the final hidden state for a batch as the initial hidden state of the next batch. The final hidden state for the first batch has to have exactly the same shape as the initial hidden state of the next batch, which requires that batch size stay the same across batches.</p>
    <p>When you set the batch size to 64, <code>model.fit</code> will use the remaining data at the end of an epoch as a batch, and this may not have up to 64 datapoints. So, you get such an error because the batch size is different from what the stateful LSTM expects. You don't have the problem with batch size of 1 because any remaining data at the end of an epoch will always contain exactly 1 datapoint, so no errors. More generally, 1 is always a divisor of any integer. So, if you picked any other divisor of your data size, you should not get the error.</p>
    <p>In the error message you posted, it appears the last batch has size of 49 instead of 64. On a side note: The reason the shapes look different from the input is because, under the hood, keras works with the tensors in time_major (i.e. the first axis is for steps of sequence). When you pass a tensor of shape (10, 15, 2) that represents (batch_size, steps_per_sequence, num_features), keras reshapes it to (15, 10, 2) under the hood.</p>
        </div>
        <div class="mt24">
            <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
                <time itemprop="dateCreated" datetime="2020-10-20T00:15:29"></time>
                <div class="flex--item mr16" style="flex: 1 1 100px;">
                    
    
    
    <div class="js-post-menu pt2" data-post-id="64436749" data-post-type-id="2">
    
        <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">
    
            <div class="flex--item">
                <a href="/a/64436749"
                   rel="nofollow"
                   itemprop="url"
                   class="js-share-link js-gps-track"
                   title="Short permalink to this answer"
                   data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })"
                   data-controller="se-share-sheet"
                   data-se-share-sheet-title="Share a link to this answer"
                   data-se-share-sheet-subtitle=""
                   data-se-share-sheet-post-type="answer"
                   data-se-share-sheet-social="facebook twitter devto"
                   data-se-share-sheet-location="2"
                   data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f4.0%2f"
                   data-se-share-sheet-license-name="CC BY-SA 4.0"
                   data-s-popover-placement="bottom-start">Share</a>
            </div>
    
    
    
                    <div class="flex--item">
                        <button type="button"
                                id="btnFollowPost-64436749" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track"
                                data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })"
                                data-controller="s-tooltip " data-s-tooltip-placement="bottom"
                                data-s-popover-placement="bottom" aria-controls=""
                                title="Follow this answer to receive notifications">
                            Follow
                            <input type="hidden" id="voteFollowHash" value="70:3:31e,16:26d4ea152e11a9eb,10:1715767546,16:b25f173f7002f286,8:64436749,cf4262b32154aa58e3ba612c5efdc223087515cf5a9437442c44ffc80ff97003" />
                        </button>
                    </div>
    
    
    
    
    
    
        </div>
        <div class="js-menu-popup-container"></div>
    </div>
                </div>
                <div class="post-signature flex--item fl0">
    <div class="user-info ">
        <div class="d-flex ">
            <div class="user-action-time fl-grow1">
                <a href="/posts/64436749/revisions" title="show all edits to this post"
                             class="js-gps-track"
                             data-gps-track="post.click({ item: 4, priv: 0, post_type: 2 })">edited <span title='2020-10-20 19:11:42Z' class='relativetime'>Oct 20, 2020 at 19:11</span></a>
            </div>
            
        </div>
        <div class="user-gravatar32">
            
        </div>
        <div class="user-details">
            
            <div class="-flair">
                
            </div>
        </div>
    </div>
                </div>
    
    
                <div class="post-signature flex--item fl0">
                    <div class="user-info ">
        <div class="d-flex ">
            <div class="user-action-time fl-grow1">
                answered <span title='2020-10-20 00:15:29Z' class='relativetime'>Oct 20, 2020 at 0:15</span>
            </div>
            
        </div>
        <div class="user-gravatar32">
            <a href="/users/9808917/princy"><div class="gravatar-wrapper-32"><img src="https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg?sz=64" alt="Princy&#39;s user avatar" width="32" height="32" class="bar-sm"></div></a>
        </div>
        <div class="user-details" itemprop="author" itemscope itemtype="http://schema.org/Person">
            <a href="/users/9808917/princy">Princy</a><span class="d-none" itemprop="name">Princy</span>
            <div class="-flair">
                <span class="reputation-score" title="reputation score " dir="ltr">343</span><span title="3 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">3</span></span><span class="v-visible-sr">3 silver badges</span><span title="11 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">11</span></span><span class="v-visible-sr">11 bronze badges</span>
            </div>
        </div>
    </div>
    
    
                </div>
            </div>
            
        
        </div>
        
    </div>
    
    
    
    
                <span class="d-none" itemprop="commentCount">5</span> 
        <div class="post-layout--right js-post-comments-component">
            <div id="comments-64436749" class="comments js-comments-container bt bc-black-200 mt12 " data-post-id="64436749" data-min-length="15">
                <ul class="comments-list js-comments-list"
                        data-remaining-comments-count="0"
                        data-canpost="false"
                        data-cansee="true"
                        data-comments-unavailable="false"
                        data-addlink-disabled="true">
    
                            <li id="comment-114013899" class="comment js-comment " data-comment-id="114013899" data-comment-owner-id="14055413" data-comment-score="0">
            <div class="js-comment-actions comment-actions">
                <div class="comment-score js-comment-score js-comment-edit-hide">
                </div>
            </div>
            <div class="comment-text  js-comment-text-and-form">
                <div class="comment-body js-comment-edit-hide">
                    
                    <span class="comment-copy">Thanks for the very comprehensive explanation! I think now I understand the problem</span>
                    
                    <div class="d-inline-flex ai-center">
    &ndash;&nbsp;<a href="/users/14055413/glorian"
                                    title="53 reputation"
                                    class="comment-user owner">glorian</a>
                    </div>
                    <span class="comment-date" dir="ltr"><span title='2020-10-22 09:10:55Z, License: CC BY-SA 4.0' class='relativetime-clean'>Oct 22, 2020 at 9:10</span></span>
                </div>
            </div>
        </li>
        <li id="comment-114064926" class="comment js-comment " data-comment-id="114064926" data-comment-owner-id="9808917" data-comment-score="0">
            <div class="js-comment-actions comment-actions">
                <div class="comment-score js-comment-score js-comment-edit-hide">
                </div>
            </div>
            <div class="comment-text  js-comment-text-and-form">
                <div class="comment-body js-comment-edit-hide">
                    
                    <span class="comment-copy">@glorian If the answer helped with the problem, please accept it and or upvote. If you have followup questions, feel free to ask.</span>
                    
                    <div class="d-inline-flex ai-center">
    &ndash;&nbsp;<a href="/users/9808917/princy"
                                    title="343 reputation"
                                    class="comment-user">Princy</a>
                    </div>
                    <span class="comment-date" dir="ltr"><span title='2020-10-23 22:43:10Z, License: CC BY-SA 4.0' class='relativetime-clean'>Oct 23, 2020 at 22:43</span></span>
                </div>
            </div>
        </li>
        <li id="comment-118623853" class="comment js-comment " data-comment-id="118623853" data-comment-owner-id="11829398" data-comment-score="0">
            <div class="js-comment-actions comment-actions">
                <div class="comment-score js-comment-score js-comment-edit-hide">
                </div>
            </div>
            <div class="comment-text  js-comment-text-and-form">
                <div class="comment-body js-comment-edit-hide">
                    
                    <span class="comment-copy">@Princy why do you do <code>train_data.repeat()</code> and <code>val_data.repeat()</code> in the first few code snippets? Does this ensure that the last elements not included in the first epoch are the first elements in the second epoch?</span>
                    
                    <div class="d-inline-flex ai-center">
    &ndash;&nbsp;<a href="/users/11829398/codeananda"
                                    title="1,155 reputation"
                                    class="comment-user">codeananda</a>
                    </div>
                    <span class="comment-date" dir="ltr"><span title='2021-04-15 14:42:43Z, License: CC BY-SA 4.0' class='relativetime-clean'>Apr 15, 2021 at 14:42</span></span>
                </div>
            </div>
        </li>
        <li id="comment-118624003" class="comment js-comment " data-comment-id="118624003" data-comment-owner-id="11829398" data-comment-score="0">
            <div class="js-comment-actions comment-actions">
                <div class="comment-score js-comment-score js-comment-edit-hide">
                </div>
            </div>
            <div class="comment-text  js-comment-text-and-form">
                <div class="comment-body js-comment-edit-hide">
                    
                    <span class="comment-copy">Also @Princy why repeat the dataset if you are going to drop the remainder? Does it not work if you keep the remainder? Then you would train on a slightly different dataset on each epoch.</span>
                    
                    <div class="d-inline-flex ai-center">
    &ndash;&nbsp;<a href="/users/11829398/codeananda"
                                    title="1,155 reputation"
                                    class="comment-user">codeananda</a>
                    </div>
                    <span class="comment-date" dir="ltr"><span title='2021-04-15 14:47:47Z, License: CC BY-SA 4.0' class='relativetime-clean'>Apr 15, 2021 at 14:47</span></span>
                </div>
            </div>
        </li>
        <li id="comment-118941793" class="comment js-comment " data-comment-id="118941793" data-comment-owner-id="9808917" data-comment-score="1">
            <div class="js-comment-actions comment-actions">
                <div class="comment-score js-comment-score js-comment-edit-hide">
                        <span title="number of &#x27;useful comment&#x27; votes received"
                                class="cool">1</span>
                </div>
            </div>
            <div class="comment-text  js-comment-text-and-form">
                <div class="comment-body js-comment-edit-hide">
                    
                    <span class="comment-copy">@AdamMurphy the <code>repeat</code> method, invoked with the default argument <code>count=None</code>, makes the data to be streamed infinitely. And when to stop is then controlled via the arguments of the <code>fit</code> method of the model, in particular <code>steps_per_epoch</code> and <code>epoch</code> (training ends when the specified <code>epoch</code> is reached, and <code>steps_per_epoch</code> specify how many datapoints make up an epoch). This is just one approach to feed data to a tensorflow model. There are other ways that work just as fine, or some may be better suited for certain cases. You can still use <code>drop_remainder</code> without <code>repeat</code></span>
                    
                    <div class="d-inline-flex ai-center">
    &ndash;&nbsp;<a href="/users/9808917/princy"
                                    title="343 reputation"
                                    class="comment-user">Princy</a>
                    </div>
                    <span class="comment-date" dir="ltr"><span title='2021-04-27 21:59:58Z, License: CC BY-SA 4.0' class='relativetime-clean'>Apr 27, 2021 at 21:59</span></span>
                            <span title="this comment was edited 2 times">
                                <svg aria-hidden="true" class="va-text-bottom o50 svg-icon iconPencilSm" width="14" height="14"  viewBox="0 0 14 14"><path fill="#F1B600" d="m2 10.12 6.37-6.43 1.88 1.88L3.88 12H2v-1.88Z"/><path fill="#E87C87" d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0Z"/></svg>
                            </span>
                </div>
            </div>
        </li>
    
                </ul>
            </div>
    
            <div id="comments-link-64436749" data-rep=50 data-anon=true>
                        <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like &#x201C;&#x2B;1&#x201D; or &#x201C;thanks&#x201D;."  href="#" role="button">Add a comment</a>
                    <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
                <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href=# onclick="" role="button"></a>
            </div>         
        </div>
        </div>
    </div>
    
    <div class="js-zone-container zone-container-main">
        <div id="dfp-bmlb" class="everyonelovesstackoverflow everyoneloves__bot-mid-leaderboard everyoneloves__leaderboard"></div>
            <div class="js-report-ad-button-container " style="width: 728px"></div>
    </div>
    
                            <a name='new-answer'></a>
                                <form id="post-form" action="/questions/64159777/answer/submit" method="post" class="js-add-answer-component post-form">
                                    <input type="hidden" id="post-id" value="64159777" />
                                    <input type="hidden" id="qualityBanWarningShown" name="qualityBanWarningShown" value="false" />
                                    <input type="hidden" name="referrer" value="https://www.google.com/" />
                                    <h2 class="space" id="your-answer-header">
                                        Your Answer
                                    </h2>
                                        
    
        <script>
            StackExchange.ifUsing("editor", function () {
                StackExchange.using("externalEditor", function () {
                    StackExchange.using("snippets", function () {
                        StackExchange.snippets.init();
                    });
                });
            }, "code-snippets");
        </script>
    
    
    <script>
        StackExchange.ready(function() {
            var channelOptions = {
                tags: "".split(" "),
                id: "1"
            };
            initTagRenderer("".split(" "), "".split(" "), channelOptions);
    
            StackExchange.using("externalEditor", function() {
                // Have to fire editor after snippets, if snippets enabled
                if (StackExchange.settings.snippets.snippetsEnabled) {
                    StackExchange.using("snippets", function() {
                        createEditor();
                    });
                }
                else {
                    createEditor();
                }
            });
    
            function createEditor() {
                StackExchange.prepareEditor({
                    useStacksEditor: false,
                    heartbeatType: 'answer',
                    autoActivateHeartbeat: false,
                    convertImagesToLinks: true,
                    noModals: true,
                    showLowRepImageUploadWarning: true,
                    reputationToPostImages: 10,
                    bindNavPrevention: true,
                    postfix: "",
                    imageUploadEnabled: false,
                    imageUploader: {
                        brandingHtml: "",
                        contentPolicyHtml: "User contributions licensed under \u003ca href=\"https://stackoverflow.com/help/licensing\"\u003eCC BY-SA\u003c/a\u003e \u003ca href=\"https://stackoverflow.com/legal/acceptable-use-policy\"\u003e(content policy)\u003c/a\u003e",
                        allowUrls: true,
                    },
                    onDemand: true,
                    discardSelector: ".discard-answer",
                    enableTables: true,
                    isStacksEditorPreviewEnabled: false
                    ,enableTables:true,enableSnippets:true
                });
                        }
        });
    </script>
    <div id="post-editor" class="post-editor js-post-editor">
    
    
            <div class="ps-relative">
                <div class="wmd-container mb8">
                    <div id="wmd-button-bar" class="wmd-button-bar btr-sm"></div>
                        <div class="ai-content-policy-notice js-ai-policy-notice fc-black p8 bl br bc-black-300 d-none" aria-hidden="true">
                            <div class="d-flex jc-space-between ac-center gsx gs2">
                                <p class="flex--item as-center"><b>Reminder:</b> Answers generated by artificial intelligence tools are not allowed on Stack Overflow. <a href="/help/gen-ai-policy">Learn more</a></p>
                                <button class="flex--item js-dismiss-ai-banner s-btn s-btn__sm s-btn__icon fc-black"><svg aria-hidden="true" class="svg-icon iconClearSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M12 3.41 10.59 2 7 5.59 3.41 2 2 3.41 5.59 7 2 10.59 3.41 12 7 8.41 10.59 12 12 10.59 8.41 7 12 3.41Z"/></svg></button>
                            </div>
                        </div>
                        <input type="hidden" name="AIPolicyNoticeShown" value="true"/>
                    <div class="js-stacks-validation">
                        <div class="ps-relative">
                            <textarea id="wmd-input"
                                      name="post-text"
                                      class="wmd-input s-input bar0 js-post-body-field"
                                      data-editor-type="wmd"
                                      data-post-type-id="2"
                                      cols="92" rows="15"
                                      aria-labelledby="your-answer-header"
                                      tabindex="101"
                                      data-min-length=""></textarea>
                        </div>
                        <div class="s-input-message mt4 d-none js-stacks-validation-message"></div>
                    </div>
                </div>
            </div>
    
        <aside class="d-flex ai-start jc-space-between js-answer-help s-notice s-notice__warning pb0 pr4 pt4 mb8 d-none" role="status" aria-hidden="true">
        <div class="flex--item pt8">
            <p>Thanks for contributing an answer to Stack Overflow!</p><ul><li>Please be sure to <em>answer the question</em>. Provide details and share your research!</li></ul><p>But <em>avoid</em> …</p><ul><li>Asking for help, clarification, or responding to other answers.</li><li>Making statements based on opinion; back them up with references or personal experience.</li></ul><p>To learn more, see our <a href="/help/how-to-answer">tips on writing great answers</a>.</p>
        </div>
        <button class="flex--item js-answer-help-close-btn s-btn s-btn__muted fc-black-600">
            <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18"  viewBox="0 0 18 18"><path  d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9 15 4.41Z"/></svg>
        </button>
    </aside>
    
    
    
        <div>
            <div id="draft-saved" class="fc-success h24" style="display:none;">Draft saved</div>
            <div id="draft-discarded" class="fc-error h24" style="display:none;">Draft discarded</div>
        </div>
    
    
                <div id="wmd-preview" class="s-prose mb16 wmd-preview js-wmd-preview"></div>
                <div></div>
    
            <div class="edit-block">
                <input id="fkey" name="fkey" type="hidden" value="4a4af90770b3a1e583cccae29b6b66c55d0409a14103bc5d312f983c6775f325">
                <input id="author" name="author" type="text">
            </div>
    
    </div>
    
    
                                    <div class="ps-relative">
                                                    <div class="form-item dno new-post-login p0 my16">
                    <div class="d-flex gs16 md:fd-column new-login-form">
                        <div class="d-flex fd-column w50 md:w-auto gsy gs8 jc-space-between new-login-left">
                            <h3 class="flex--item fs-title">Sign up or <a id="login-link" href="/users/login?ssrc=question_page&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f64159777%2fstateful-lstm-tensorflow-invalid-input-h-shape-error%23new-answer">log in</a></h3>
                            <script>
                                StackExchange.ready(function () {
                                    StackExchange.helpers.onClickDraftSave('#login-link');
    
                                    var $window = $(window),
                                        onScroll = function(e) {
                                            var $elem = $('.new-login-left'),
                                                docViewTop = $window.scrollTop(),
                                                docViewBottom = docViewTop + $window.height(),
                                                elemTop = $elem.offset().top,
                                                elemBottom = elemTop + $elem.height();
                                            if ((docViewTop < elemTop) && (docViewBottom > elemBottom))  {
                                                StackExchange.using('gps', function() { StackExchange.gps.track('embedded_signup_form.view', { location: 'question_page' }); });
                                                $window.off('scroll', onScroll);
                                            }
                                        };
                                    $window.on('scroll', onScroll);
                                                                    });
                            </script>
                            <div class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon google-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Started - Google&quot;,&quot;New Post&quot;,null,null]">
                                <svg aria-hidden="true" class="native svg-icon iconGoogle" width="18" height="18"  viewBox="0 0 18 18"><path fill="#4285F4" d="M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 0 0 2.38-5.88c0-.57-.05-.66-.15-1.18Z"/><path fill="#34A853" d="M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 0 1-7.18-2.54H1.83v2.07A8 8 0 0 0 8.98 17Z"/><path fill="#FBBC05" d="M4.5 10.52a4.8 4.8 0 0 1 0-3.04V5.41H1.83a8 8 0 0 0 0 7.18l2.67-2.07Z"/><path fill="#EA4335" d="M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 0 0 1.83 5.4L4.5 7.49a4.77 4.77 0 0 1 4.48-3.3Z"/></svg> Sign up using Google
                            </div>
                            <div class="flex--item s-btn s-btn__muted s-btn__icon facebook-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Started - Facebook&quot;,&quot;New Post&quot;,null,null]">
                                <svg aria-hidden="true" class="svg-icon iconFacebook" width="18" height="18"  viewBox="0 0 18 18"><path fill="#4167B2" d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3Zm6.55 16v-6.2H7.46V8.4h2.09V6.61c0-2.07 1.26-3.2 3.1-3.2.88 0 1.64.07 1.87.1v2.16h-1.29c-1 0-1.19.48-1.19 1.18V8.4h2.39l-.31 2.42h-2.08V17h-2.5Z"/></svg> Sign up using Facebook
                            </div>
                            <div class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon stackexchange-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;New Post&quot;,null,null]">
                                <svg aria-hidden="true" class="native svg-icon iconLogoGlyphXSm" width="18" height="18" viewBox="0 0 18 18"><path d="M14 16v-5h2v7H2v-7h2v5h10Z" fill="#BCBBBB"/><path d="m12.09.72-1.21.9 4.5 6.07 1.22-.9L12.09.71ZM5 15h8v-2H5v2Zm9.15-5.87L8.35 4.3l.96-1.16 5.8 4.83-.96 1.16Zm-7.7-1.47 6.85 3.19.63-1.37-6.85-3.2-.63 1.38Zm6.53 5L5.4 11.39l.38-1.67 7.42 1.48-.22 1.46Z" fill="#F48024"/></svg> Sign up using Email and Password
                            </div>
                        </div>
                        <input type="hidden" name="use-facebook" class="use-facebook" value="false" />
                        <input type="hidden" name="use-google" class="use-google" value="false" />
                        <button type="button" class="d-none js-submit-openid">Submit</button>
                        <div class="d-flex gsy gs8 fd-column w50 md:w-auto new-login-right form-item p0">
                                    <h3 class="flex--item fs-title">Post as a guest</h3>
                <div class="flex--item">
                    <div class="d-flex gs4 gsy fd-column">
                        <label class="s-label" for="display-name">Name</label>
                        <div class="d-flex ps-relative">
                            <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="" />
                        </div>
                    </div>
                </div>
                <div class="flex--item">
                    <div class="d-flex gs4 gsy fd-column">
                        <div class="flex--item">
                            <div class="d-flex gs2 gsy fd-column">
                                <label class="flex--item s-label" for="m-address">Email</label>
                                <p class="flex--item s-description">Required, but never shown</p>
                            </div>
                        </div>
                        <div class="d-flex ps-relative">
                            <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="" />
                        </div>
                    </div>
                </div>
    
                        </div>
                    </div>
                </div>
                <script>
                    StackExchange.ready(
                        function () {
                            StackExchange.openid.initPostLogin('.new-post-login', 'https%3a%2f%2fstackoverflow.com%2fquestions%2f64159777%2fstateful-lstm-tensorflow-invalid-input-h-shape-error%23new-answer', 'question_page');
                        }
                    );
                </script>
                <noscript>
                            <h3 class="flex--item fs-title">Post as a guest</h3>
                <div class="flex--item">
                    <div class="d-flex gs4 gsy fd-column">
                        <label class="s-label" for="display-name">Name</label>
                        <div class="d-flex ps-relative">
                            <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="" />
                        </div>
                    </div>
                </div>
                <div class="flex--item">
                    <div class="d-flex gs4 gsy fd-column">
                        <div class="flex--item">
                            <div class="d-flex gs2 gsy fd-column">
                                <label class="flex--item s-label" for="m-address">Email</label>
                                <p class="flex--item s-description">Required, but never shown</p>
                            </div>
                        </div>
                        <div class="d-flex ps-relative">
                            <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="" />
                        </div>
                    </div>
                </div>
    
                </noscript>
    
                                    </div>
    
                                        <div class="form-submit clear-both d-flex gsx gs4">
                                            <button id="submit-button" class="flex--item s-btn s-btn__filled s-btn__icon" type="submit" tabindex="120" autocomplete="off">
                                                Post Your Answer
                                            </button>
                                            <button class="flex--item s-btn s-btn__danger discard-answer dno">
                                                Discard
                                            </button>
                                                <p class="privacy-policy-agreement">
                                                    By clicking “Post Your Answer”, you agree to our <a href='https://stackoverflow.com/legal/terms-of-service/public' name='tos' target='_blank' class='-link'>terms of service</a> and acknowledge you have read our <a href='https://stackoverflow.com/legal/privacy-policy' name='privacy' target='_blank' class='-link'>privacy policy</a>.<input type="hidden" name="legalLinksShown" value="1" />
                                                </p>
                                        </div>
                                        <div class="js-general-error general-error clear-both d-none" aria-live="polite"></div>
                                </form>
    
    
                                <h2 class="bottom-notice" data-loc="1">
                                    <div>
    Not the answer you&#x27;re looking for? Browse other questions tagged <ul class='ml0 list-ls-none js-post-tag-list-wrapper d-inline'><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/tensorflow" class="post-tag" title="show questions tagged &#39;tensorflow&#39;" aria-label="show questions tagged &#39;tensorflow&#39;" rel="tag" aria-labelledby="tag-tensorflow-tooltip-container" data-tag-menu-origin="Unknown">tensorflow</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/keras" class="post-tag" title="show questions tagged &#39;keras&#39;" aria-label="show questions tagged &#39;keras&#39;" rel="tag" aria-labelledby="tag-keras-tooltip-container" data-tag-menu-origin="Unknown">keras</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/neural-network" class="post-tag" title="show questions tagged &#39;neural-network&#39;" aria-label="show questions tagged &#39;neural-network&#39;" rel="tag" aria-labelledby="tag-neural-network-tooltip-container" data-tag-menu-origin="Unknown">neural-network</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/lstm" class="post-tag" title="show questions tagged &#39;lstm&#39;" aria-label="show questions tagged &#39;lstm&#39;" rel="tag" aria-labelledby="tag-lstm-tooltip-container" data-tag-menu-origin="Unknown">lstm</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/lstm-stateful" class="post-tag" title="show questions tagged &#39;lstm-stateful&#39;" aria-label="show questions tagged &#39;lstm-stateful&#39;" rel="tag" aria-labelledby="tag-lstm-stateful-tooltip-container" data-tag-menu-origin="Unknown">lstm-stateful</a></li></ul> or <a href="/questions/ask">ask your own question</a>.                                </div>
                                </h2>
                    </div>
                </div>
    
                
    <div id="sidebar" class="show-votes" role="complementary" aria-label="sidebar">
            
    
        
        <div class="s-sidebarwidget s-sidebarwidget__yellow s-anchors s-anchors__grayscale mb16" data-tracker="cb=1">
            <ul class="d-block p0 m0">
                            <li class="s-sidebarwidget--header s-sidebarwidget__small-bold-text d-flex fc-black-500 d:fc-black-600 bb bbw1">
                                The Overflow Blog
                            </li>
            <li class="s-sidebarwidget--item d-flex px16">
                <div class="flex--item1 fl-shrink0">
    <svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14"  viewBox="0 0 14 14"><path fill="#F1B600" d="m2 10.12 6.37-6.43 1.88 1.88L3.88 12H2v-1.88Z"/><path fill="#E87C87" d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0Z"/></svg>            </div>
                <div class="flex--item wmn0 ow-break-word">
                    <a href="https://stackoverflow.blog/2024/05/13/why-do-only-a-small-percentage-of-genai-projects-actually-make-it-into-production/" class="js-gps-track" title="Why do only a small percentage of GenAI projects actually make it into production?" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2024/05/13/why-do-only-a-small-percentage-of-genai-projects-actually-make-it-into-production/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 0 })">Why do only a small percentage of GenAI projects actually make it into...</a>
                </div>
            </li>
            <li class="s-sidebarwidget--item d-flex px16">
                <div class="flex--item1 fl-shrink0">
    <svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14"  viewBox="0 0 14 14"><path fill="#F1B600" d="m2 10.12 6.37-6.43 1.88 1.88L3.88 12H2v-1.88Z"/><path fill="#E87C87" d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0Z"/></svg>            </div>
                <div class="flex--item wmn0 ow-break-word">
                    <a href="https://stackoverflow.blog/2024/05/14/spreading-the-gospel-of-python/" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2024/05/14/spreading-the-gospel-of-python/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 1 })">Spreading the gospel of Python</a>
                </div>
            </li>
                            <li class="s-sidebarwidget--header s-sidebarwidget__small-bold-text d-flex fc-black-500 d:fc-black-600 bb bbw1">
                                Featured on Meta
                            </li>
            <li class="s-sidebarwidget--item d-flex px16">
                <div class="flex--item1 fl-shrink0">
    <div class="favicon favicon-stackexchangemeta" title="Meta Stack Exchange"></div>            </div>
                <div class="flex--item wmn0 ow-break-word">
                    <a href="https://meta.stackexchange.com/questions/399619/our-partnership-with-openai" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackexchange.com/questions/399619/our-partnership-with-openai&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 3, position: 2 })">Our Partnership with OpenAI</a>
                </div>
            </li>
            <li class="s-sidebarwidget--item d-flex px16">
                <div class="flex--item1 fl-shrink0">
    <div class="favicon favicon-stackexchangemeta" title="Meta Stack Exchange"></div>            </div>
                <div class="flex--item wmn0 ow-break-word">
                    <a href="https://meta.stackexchange.com/questions/399662/imgur-image-url-migration-coming-soon-to-a-stack-exchange-site-near-you" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackexchange.com/questions/399662/imgur-image-url-migration-coming-soon-to-a-stack-exchange-site-near-you&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 3, position: 3 })">Imgur image URL migration: Coming soon to a Stack Exchange site near you!</a>
                </div>
            </li>
            <li class="s-sidebarwidget--item d-flex px16">
                <div class="flex--item1 fl-shrink0">
    <div class="favicon favicon-stackoverflowmeta" title="Meta Stack Overflow"></div>            </div>
                <div class="flex--item wmn0 ow-break-word">
                    <a href="https://meta.stackoverflow.com/questions/422645/the-price-tag-is-being-burninated" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackoverflow.com/questions/422645/the-price-tag-is-being-burninated&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 6, position: 4 })">The [price] tag is being burninated</a>
                </div>
            </li>
            <li class="s-sidebarwidget--item d-flex px16">
                <div class="flex--item1 fl-shrink0">
    <div class="favicon favicon-stackoverflowmeta" title="Meta Stack Overflow"></div>            </div>
                <div class="flex--item wmn0 ow-break-word">
                    <a href="https://meta.stackoverflow.com/questions/421831/policy-generative-ai-e-g-chatgpt-is-banned" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackoverflow.com/questions/421831/policy-generative-ai-e-g-chatgpt-is-banned&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 6, position: 5 })">Policy: Generative AI (e.g., ChatGPT) is banned</a>
                </div>
            </li>
            </ul>
        </div>
    
    
    <div class="js-zone-container zone-container-sidebar">
        <div id="dfp-tsb" class="everyonelovesstackoverflow everyoneloves__top-sidebar"></div>
            <div class="js-report-ad-button-container " style="width: 300px"></div>
    </div>
    <div class="js-zone-container zone-container-sidebar">
        <div id="dfp-msb" class="everyonelovesstackoverflow everyoneloves__mid-sidebar"></div>
            <div class="js-report-ad-button-container " style="width: 300px"></div>
    </div>
    <div id="hireme"></div>        
    
        
    
    
            <div class="module sidebar-related">
                <h4 id="h-related">Related</h4>
                <div class="related js-gps-related-questions" data-tracker="rq=3">
                        <div class="spacer" data-question-id="39298462">
                            <a href="/q/39298462" title="Question score (upvotes - downvotes)" >
                                <div class="answer-votes answered-accepted default">4</div>
                            </a>
                            <a href="/questions/39298462/keras-stateful-lstm-error" class="question-hyperlink">Keras stateful LSTM error</a>
                        </div>
                        <div class="spacer" data-question-id="45949577">
                            <a href="/q/45949577" title="Question score (upvotes - downvotes)" >
                                <div class="answer-votes default">1</div>
                            </a>
                            <a href="/questions/45949577/error-in-stateful-convolutional-lstm" class="question-hyperlink">Error in Stateful Convolutional LSTM</a>
                        </div>
                        <div class="spacer" data-question-id="47062577">
                            <a href="/q/47062577" title="Question score (upvotes - downvotes)" >
                                <div class="answer-votes answered-accepted default">1</div>
                            </a>
                            <a href="/questions/47062577/error-when-using-batch-input-shape-for-stateful-lstm-in-rnn" class="question-hyperlink">Error when using batch_input_shape for stateful LSTM in RNN</a>
                        </div>
                        <div class="spacer" data-question-id="49842207">
                            <a href="/q/49842207" title="Question score (upvotes - downvotes)" >
                                <div class="answer-votes answered-accepted default">1</div>
                            </a>
                            <a href="/questions/49842207/valueerror-in-case-of-lstm-with-stateful-true" class="question-hyperlink">ValueError: in case of LSTM with `stateful=True`</a>
                        </div>
                        <div class="spacer" data-question-id="49847379">
                            <a href="/q/49847379" title="Question score (upvotes - downvotes)" >
                                <div class="answer-votes answered-accepted default">0</div>
                            </a>
                            <a href="/questions/49847379/indexerror-lstm-with-stateful-true" class="question-hyperlink">IndexError: LSTM with &quot;stateful=True&quot;</a>
                        </div>
                        <div class="spacer" data-question-id="57380982">
                            <a href="/q/57380982" title="Question score (upvotes - downvotes)" >
                                <div class="answer-votes default">1</div>
                            </a>
                            <a href="/questions/57380982/using-lstm-error-when-checking-input-expected-lstm-22-input-to-have-3-dimensio" class="question-hyperlink">Using LSTM &quot;Error when checking input: expected lstm_22_input to have 3 dimensions, but got array with shape (15, 33297)&quot;</a>
                        </div>
                        <div class="spacer" data-question-id="61871071">
                            <a href="/q/61871071" title="Question score (upvotes - downvotes)" >
                                <div class="answer-votes answered-accepted default">3</div>
                            </a>
                            <a href="/questions/61871071/keras-lstm-incorrect-input-shape" class="question-hyperlink">keras lstm incorrect input_shape</a>
                        </div>
                        <div class="spacer" data-question-id="68323793">
                            <a href="/q/68323793" title="Question score (upvotes - downvotes)" >
                                <div class="answer-votes answered-accepted default">1</div>
                            </a>
                            <a href="/questions/68323793/keras-lstm-input-valueerror-shapes-are-incompatible" class="question-hyperlink">Keras LSTM input ValueError: Shapes are incompatible</a>
                        </div>
                        <div class="spacer" data-question-id="71251340">
                            <a href="/q/71251340" title="Question score (upvotes - downvotes)" >
                                <div class="answer-votes answered-accepted default">2</div>
                            </a>
                            <a href="/questions/71251340/keras-stateful-lstm-error-specified-a-list-with-shape-4-1-from-a-tensor-with" class="question-hyperlink">Keras stateful LSTM error: Specified a list with shape [4,1] from a tensor with shape [32,1]</a>
                        </div>
                        <div class="spacer" data-question-id="75217510">
                            <a href="/q/75217510" title="Question score (upvotes - downvotes)" >
                                <div class="answer-votes default">0</div>
                            </a>
                            <a href="/questions/75217510/valueerror-in-model-fit-in-lstm" class="question-hyperlink">ValueError in model.fit in lstm</a>
                        </div>
                </div>
            </div>
            <script type="text/javascript">
                     $(function() {
                         $(".js-gps-related-questions .spacer").on("click", function () {
                            fireRelatedEvent($(this).index() + 1, $(this).data('question-id'));
                         });
    
                     function fireRelatedEvent(position, questionId) {
                         StackExchange.using("gps", function() {
                             StackExchange.gps.track('related_questions.click',
                             {
                                 position: position,
                                 originQuestionId: 64159777,
                                 relatedQuestionId: +questionId,
                                 location: 'sidebar',
                                 source: 'Baseline'
                             });    
                         });
                     }
                 });
             </script>
    
    
    
        <div id="hot-network-questions" class="module tex2jax_ignore">
        <h4>
            <a href="https://stackexchange.com/questions?tab=hot"
               class="js-gps-track s-link s-link__inherit" 
               data-gps-track="posts_hot_network.click({ item_type:1, location:11 })">
                Hot Network Questions
            </a>
        </h4>
        <ul>
                <li >
                    <div class="favicon favicon-gaming" title="Arqade"></div><a href="https://gaming.stackexchange.com/questions/408128/what-is-this-nintendo-64-dd-flyswatter-game-from" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:41 }); posts_hot_network.click({ item_type:2, location:11 })">
                        What is this Nintendo 64 DD flyswatter game from?
                    </a>
    
                </li>
                <li >
                    <div class="favicon favicon-opensource" title="Open Source Stack Exchange"></div><a href="https://opensource.stackexchange.com/questions/14790/allow-commercial-use-but-require-removal-of-company-name" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:619 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Allow commercial use, but require removal of company name
                    </a>
    
                </li>
                <li >
                    <div class="favicon favicon-askubuntu" title="Ask Ubuntu"></div><a href="https://askubuntu.com/questions/1514031/install-tp-link-archer-t2u-v3-driver-in-ubuntu-without-internet" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:89 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Install TP-Link Archer T2U V3 driver in Ubuntu without internet
                    </a>
    
                </li>
                <li >
                    <div class="favicon favicon-travel" title="Travel Stack Exchange"></div><a href="https://travel.stackexchange.com/questions/189023/timetable-for-cercanias-am-narrow-gauge-railway-in-spain" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:273 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Timetable for Cercanias AM narrow gauge railway in Spain
                    </a>
    
                </li>
                <li >
                    <div class="favicon favicon-mathoverflow" title="MathOverflow"></div><a href="https://mathoverflow.net/questions/471217/does-this-sequence-ever-end" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:504 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Does this sequence ever end?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-law" title="Law Stack Exchange"></div><a href="https://law.stackexchange.com/questions/102609/what-happens-to-a-trial-if-the-presiding-judge-is-unable-to-finish-the-trial" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:617 }); posts_hot_network.click({ item_type:2, location:11 })">
                        What happens to a trial if the presiding judge is unable to finish the trial?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-christianity" title="Christianity Stack Exchange"></div><a href="https://christianity.stackexchange.com/questions/101638/where-can-i-find-a-jehovahs-witnesses-version-of-a-hebrew-interlinear-old-testa" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:304 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Where can I find a Jehovah&#x27;s Witnesses version of a Hebrew Interlinear Old Testament?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-money" title="Personal Finance &amp; Money Stack Exchange"></div><a href="https://money.stackexchange.com/questions/162612/how-s-the-interest-adjusted-for-additional-principal-payment" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:93 }); posts_hot_network.click({ item_type:2, location:11 })">
                        How&#x2019;s the interest adjusted for additional Principal payment?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-codereview" title="Code Review Stack Exchange"></div><a href="https://codereview.stackexchange.com/questions/292060/brocards-conjecture-candidate-finder" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:196 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Brocard&#x27;s Conjecture Candidate Finder
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-ell" title="English Language Learners Stack Exchange"></div><a href="https://ell.stackexchange.com/questions/352072/how-to-use-double-as-a-verb" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:481 }); posts_hot_network.click({ item_type:2, location:11 })">
                        How to use DOUBLE as a verb
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-politics" title="Politics Stack Exchange"></div><a href="https://politics.stackexchange.com/questions/87454/why-does-the-usa-ask-nato-partners-to-donate-patriot-missile-systems-to-ukraine" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:475 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Why does the USA ask NATO partners to donate Patriot missile systems to Ukraine and not donate them itself?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-cs" title="Computer Science Stack Exchange"></div><a href="https://cs.stackexchange.com/questions/168067/how-to-solve-a-system-of-xor-equations-in-a-cyclic-graph" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:419 }); posts_hot_network.click({ item_type:2, location:11 })">
                        How to solve a system of XOR equations in a cyclic graph?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-tex" title="TeX - LaTeX Stack Exchange"></div><a href="https://tex.stackexchange.com/questions/717944/not-displaying-bold-chinese-character-in-times-new-roman-font" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:85 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Not displaying bold chinese character in Times New Roman font
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-mathoverflow" title="MathOverflow"></div><a href="https://mathoverflow.net/questions/471247/differing-monoidal-model-structures-on-a-fixed-model-category" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:504 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Differing monoidal model structures on a fixed model category
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-music" title="Music: Practice &amp; Theory Stack Exchange"></div><a href="https://music.stackexchange.com/questions/135998/what-chord-symbol-would-you-use-to-describe-this-voicing" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:240 }); posts_hot_network.click({ item_type:2, location:11 })">
                        What chord symbol would you use to describe this voicing?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-english" title="English Language &amp; Usage Stack Exchange"></div><a href="https://english.stackexchange.com/questions/622436/proverb-for-someone-who-mistakenly-assumes-he-has-found-the-right-answer-and-is" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:97 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Proverb for someone who mistakenly assumes he has found the right answer and is unwilling to accept his error?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-worldbuilding" title="Worldbuilding Stack Exchange"></div><a href="https://worldbuilding.stackexchange.com/questions/258234/fully-electric-flamethrower" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:579 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Fully electric flamethrower
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-philosophy" title="Philosophy Stack Exchange"></div><a href="https://philosophy.stackexchange.com/questions/112996/must-a-domain-of-discourse-always-be-specified-in-universally-quantified-stateme" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:265 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Must a domain of discourse always be specified in universally quantified statements?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-diy" title="Home Improvement Stack Exchange"></div><a href="https://diy.stackexchange.com/questions/299855/i-lost-the-keys-for-a-gates-lock-where-can-i-find-a-replacement-cylinder-or-ho" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:73 }); posts_hot_network.click({ item_type:2, location:11 })">
                        I lost the keys for a gate&#x27;s lock. Where can I find a replacement cylinder or how can I get new keys?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-tex" title="TeX - LaTeX Stack Exchange"></div><a href="https://tex.stackexchange.com/questions/717958/how-to-change-default-and-in-amsart-title" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:85 }); posts_hot_network.click({ item_type:2, location:11 })">
                        How to change default &quot;and&quot; in amsart title
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-diy" title="Home Improvement Stack Exchange"></div><a href="https://diy.stackexchange.com/questions/299773/can-i-use-a-hose-clamp-to-ground-a-wire-to-emt" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:73 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Can I use a hose clamp to ground a wire to EMT?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-stats" title="Cross Validated"></div><a href="https://stats.stackexchange.com/questions/647179/for-what-kind-of-distributions-could-the-joint-distribution-be-determined-unique" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:65 }); posts_hot_network.click({ item_type:2, location:11 })">
                        For what kind of distributions could the joint distribution be determined uniquely by marginal distribution and correlation?
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-math" title="Mathematics Stack Exchange"></div><a href="https://math.stackexchange.com/questions/4916596/question-regarding-multiplication-table-of-group-of-odd-order" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:69 }); posts_hot_network.click({ item_type:2, location:11 })">
                        Question regarding multiplication table of group of odd order.
                    </a>
    
                </li>
                <li class="dno js-hidden">
                    <div class="favicon favicon-blender" title="Blender Stack Exchange"></div><a href="https://blender.stackexchange.com/questions/318300/how-can-i-separate-curve-from-profile-using-geometry-nodes" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:502 }); posts_hot_network.click({ item_type:2, location:11 })">
                        How can I separate curve from profile using Geometry Nodes?
                    </a>
    
                </li>
        </ul>
    
            <a href="#" 
               class="show-more js-show-more js-gps-track" 
               data-gps-track="posts_hot_network.click({ item_type:3, location:11 })">
                more hot questions
            </a>
    </div>
    
                    <div id="feed-link" class="js-feed-link">
            <a href="/feeds/question/64159777" title="Feed of this question and its answers">
                <svg aria-hidden="true" class="fc-orange-400 svg-icon iconRss" width="18" height="18"  viewBox="0 0 18 18"><path  d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3Zm0 1.5c6.9 0 12.5 5.6 12.5 12.5H13C13 9.55 8.45 5 3 5V2.5Zm0 5c4.08 0 7.5 3.41 7.5 7.5H8c0-2.72-2.28-5-5-5V7.5Zm0 5c1.36 0 2.5 1.14 2.5 2.5H3v-2.5Z"/></svg>
                Question feed
            </a>
        </div>
        <aside class="s-modal js-feed-link-modal" tabindex="-1" role="dialog" aria-labelledby="feed-modal-title" aria-describedby="feed-modal-description" aria-hidden="true">
            <div class="s-modal--dialog js-modal-dialog wmx4" role="document"  data-controller="se-draggable">
                <h1 class="s-modal--header fw-bold js-first-tabbable" id="feed-modal-title" data-se-draggable-target="handle" tabindex="0">
                    Subscribe to RSS
                </h1>
                <div class="d-flex gs4 gsy fd-column">
                    <div class="flex--item">
                        <label class="d-block s-label c-default" for="feed-url">
                            Question feed
                            <p class="s-description mt2" id="feed-modal-description">To subscribe to this RSS feed, copy and paste this URL into your RSS reader.</p>
                        </label>
                    </div>
                    <div class="d-flex ps-relative">
                        <input class="s-input" type="text" name="feed-url" id="feed-url" readonly="readonly" value="https://stackoverflow.com/feeds/question/64159777" />
                        <svg aria-hidden="true" class="s-input-icon fc-orange-400 svg-icon iconRss" width="18" height="18"  viewBox="0 0 18 18"><path  d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3Zm0 1.5c6.9 0 12.5 5.6 12.5 12.5H13C13 9.55 8.45 5 3 5V2.5Zm0 5c4.08 0 7.5 3.41 7.5 7.5H8c0-2.72-2.28-5-5-5V7.5Zm0 5c1.36 0 2.5 1.14 2.5 2.5H3v-2.5Z"/></svg>
                    </div>
                </div>
                <a class="s-modal--close s-btn s-btn__muted js-modal-close js-last-tabbable" href="#" aria-label="Close">
                    <svg aria-hidden="true" class="svg-icon iconClearSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M12 3.41 10.59 2 7 5.59 3.41 2 2 3.41 5.59 7 2 10.59 3.41 12 7 8.41 10.59 12 12 10.59 8.41 7 12 3.41Z"/></svg>
                </a>
            </div>
        </aside>
    
    </div>
    
        </div>
    <script>StackExchange.ready(function(){$.get('/posts/64159777/ivc/0ca9?prg=fe709cfc-caf4-4ee3-af7b-ab22ccef65a2');});</script>
    <noscript><div><img src="/posts/64159777/ivc/0ca9?prg=fe709cfc-caf4-4ee3-af7b-ab22ccef65a2" class="dno" alt="" width="0" height="0"></div></noscript><div style="display:none" id="js-codeblock-lang"></div></div>
    
                            
    
    
            </div>
        </div>
    
            
        <script type="text/javascript">
        var cam = cam || { opt: {} };
        var clcGamLoaderOptions = cam || { opt: {} };
        var opt = clcGamLoaderOptions.opt;
    
        opt.omni = 'BwoLCNDjq_OTtPo8EAUYoYDMHiACKAI6NHx0ZW5zb3JmbG93fGtlcmFzfG5ldXJhbC1uZXR3b3JrfGxzdG18bHN0bS1zdGF0ZWZ1bHxAAUgBWhIJoIuAKWhXMEsRss8ILNwzSImXlLZSx6p-ENFY';
        opt.refresh = !1;
        opt.refreshInterval = 90;
        opt.sf = !0;
        opt.hb = !1;
        opt.ll = !0;
        opt.tlb_position = 0;
        opt.personalization_consent = !0;
        opt.targeting_consent = !0;
        opt.performance_consent = !0;
    
        opt.targeting = {Registered:['false'],'so-tag':['tensorflow','keras','neural-network','lstm','lstm-stateful'],'tag-reportable':['tensorflow','keras','neural-network','lstm','lstm-stateful'],'so_tag':['tensorflow','keras','neural_network','lstm','lstm_stateful'],NumberOfAnswers:['1']};
        opt.adReportEnabled = !0;
        opt.adReportUrl = '/ads/report-ad';
        opt.adReportText = 'Report this ad';
        opt.adReportFileTypeErrorMessage = 'Please select a PNG or JPG file.';
        opt.adReportFileSizeErrorMessage = 'The file must be under 2 MiB.';
        opt.adReportErrorText = 'Error uploading ad report.';
        opt.adReportThanksText = 'Thanks for your feedback. We’ll review this against our code of conduct and take action if necessary.';
        opt.adReportLoginExpiredMessage = 'Your login session has expired, please login and try again.';
        opt.adReportLoginErrorMessage = 'An error occurred when loading the report form - please try again';
        opt.adReportModalClass = 'js-ad-report';
        opt.countryCode = 'IN';
        opt.qualtricsSurveyData = '{"isRegistered":"False","repBucket":"new","referrer":"https://stackoverflow.com/questions/64159777/stateful-lstm-tensorflow-invalid-input-h-shape-error","accountAge":"0"}';
    
            opt.brandSurveyEnabled = true;
                opt.brandSurveySettings = [{"brandId":7,"lineItemIds":[6170355049,6170355058,6170355244,6168829383,6170355787,6170355799,6168829803,6170356261,6170356282,6170984786,6170985065,6168833181,6170358871,6170360326,6170360578,6168834204,6170361016,6170986253,6377604184,6378262502,6378262511,6377604211,6377604223,6377604700,6318450889,6318453241,6318453259,6318453310],"mode":"Collect"},{"brandId":8,"lineItemIds":[6389119380,6389119404,6389119347],"mode":"Collect"},{"brandId":9,"lineItemIds":[6695878301,6695879039,6695879168,6695879174,6695879186],"mode":"Collect"},{"brandId":10,"lineItemIds":[6456294147,6456294228,6456294381,6456294396,6456294633,6456294714,6456294906,6458534116,6458539435,6458540062,6459217607,6459218636,6459219038,6459219551,6458539678,6458539864,6458539918,6459217100,6459218396,6459218846,6459219500,6459219983,6456293469,6456293664,6456293949,6459216860,6459217889,6459217904,6459218117,6459218306],"mode":"Collect"}];
        opt.perRequestGuid = 'fe709cfc-caf4-4ee3-af7b-ab22ccef65a2';
        opt.responseHash = '/6zrubHIsopATOol6Ry&#x2B;msuMI6Z6C9jlnPx5vht9sHE=';
    
    
        opt.targeting.TargetingConsent = ['True'];
        opt.allowAccountTargetingForThisRequest = !1;
    
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.has('dfptestads')) {
            const dfptestads = urlParams.get('dfptestads');
            opt.targeting.DfpTestAds = dfptestads;
        }
    </script>
    <script>;(()=>{"use strict";var __webpack_modules__={23:(e,t,s)=>{s.d(t,{Z7:()=>l,eq:()=>d,kG:()=>r});const n=(o=location.pathname,/^\/tags\//.test(o)||/^\/questions\/tagged\//.test(o)?"tag-pages":/^\/discussions\//.test(o)||/^\/beta\/discussions/.test(o)?"discussions":/^\/$/.test(o)||/^\/home/.test(o)?"home-page":/^\/jobs$/.test(o)||/^\/jobs\//.test(o)?"jobs":"question-pages");var o;let a=location.hostname;const i={slots:{lb:[[728,90]],mlb:[[728,90]],smlb:[[728,90]],bmlb:[[728,90]],sb:e=>"dfp-tsb"===e?[[300,250],[300,600]]:[[300,250]],"tag-sponsorship":[[730,135]],"mobile-below-question":[[320,50],[300,250]],msb:[[300,250],[300,600]],"talent-conversion-tracking":[[1,1]],"site-sponsorship":[[230,60]]},ids:{"dfp-tlb":"lb","dfp-mlb":"mlb","dfp-smlb":"smlb","dfp-bmlb":"bmlb","dfp-tsb":"sb","dfp-isb":"sb","dfp-tag":"tag-sponsorship","dfp-msb":"msb","dfp-sspon":"site-sponsorship","dfp-m-aq":"mobile-below-question"},idsToExcludeFromAdReports:["dfp-sspon"]};function r(){return Object.keys(i.ids)}function d(e){return i.idsToExcludeFromAdReports.indexOf(e)<0}function l(e){var t=e.split("_")[0];const s=i.ids[t];let o=i.slots[s];return"function"==typeof o&&(o=o(t)),{path:`/248424177/${a}/${s}/${n}`,sizes:o,zone:s}}},865:(e,t,s)=>{function n(e){return"string"==typeof e?document.getElementById(e):e}function o(e){return!!(e=n(e))&&"none"===getComputedStyle(e).display}function a(e){return!o(e)}function i(e){return!!e}function r(e){return/^\s*$/.test(n(e).innerHTML)}function d(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.display="none"}function l(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.display="none",[].forEach.call(e.children,l)}function c(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.removeProperty("display")}function g(e){const t=document.createElement("script");t.src=e,document.body.appendChild(t)}function p(e){return s=e,(t=[]).push=function(e){return s(),delete this.push,this.push(e)},t;var t,s}function h(e){let t="function"==typeof HTMLTemplateElement;var s=document.createElement(t?"template":"div");return e=e.trim(),s.innerHTML=e,t?s.content.firstChild:s.firstChild}s.d(t,{$Z:()=>c,Bv:()=>h,Gx:()=>g,Nj:()=>n,QZ:()=>p,cf:()=>d,pn:()=>a,wo:()=>l,xb:()=>r,xj:()=>o,yb:()=>i})},763:(__unused_webpack_module,__webpack_exports__,__webpack_require__)=>{__webpack_require__.d(__webpack_exports__,{t:()=>AdReports});var _common_helper__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(865),_console__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(276),_ad_units__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(23);class AdReports{constructor(e,t){if(this.googletag=e,this.cam=t,this.allowedFileTypes=["image/png","image/jpg","image/jpeg"],this.ignoreValidation=!1,_console__WEBPACK_IMPORTED_MODULE_1__.cM("Ad reporting init"),this.cam=t,this.callOnButtonClick=e=>this.onButtonClick(e),this.googletag.pubads().addEventListener("slotRenderEnded",e=>this.handleSlotRendered(e)),Array.isArray(t.slotsRenderedEvents)){_console__WEBPACK_IMPORTED_MODULE_1__.cM("Adding report button to "+t.slotsRenderedEvents.length+" events that have transpired");for(var s=0;s<t.slotsRenderedEvents.length;s++)this.handleSlotRendered(t.slotsRenderedEvents[s])}}handleSlotRendered(e){if(e&&e.slot&&!e.isEmpty&&(e.creativeId||e.lineItemId||!e.isEmpty)){var t=e.slot.getSlotElementId();if(t){var s=document.getElementById(t);if(s)if((0,_ad_units__WEBPACK_IMPORTED_MODULE_0__.eq)(t)){var n=s?.closest(".js-zone-container")?.querySelector(".js-report-ad-button-container");n?(n.innerHTML="",n.append(this.createButton(e)),n.style.height="24px",_console__WEBPACK_IMPORTED_MODULE_1__.cM("Added report button to the bottom of "+t)):_console__WEBPACK_IMPORTED_MODULE_1__.cM("Ad report button not found, may be intentional, element: "+t)}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of "+t+": shouldHaveReportButton = false");else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of "+t+": resolved invalid adUnit element")}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of element: invalid adUnitElementId")}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of element: invalid SlotRenderEndedEvent")}async onButtonClick(e){e.preventDefault();let t=e.target;const s=t.dataset.modalUrl,n=t.dataset.googleEventData;return await this.loadModal(s,t,n),!1}createButton(e){let t=document.createElement("button");var s=JSON.stringify(e);return t.dataset.googleEventData=s,t.dataset.modalUrl=this.cam.opt.adReportUrl,t.dataset.adUnit=e.slot.getSlotElementId(),t.classList.add("js-report-ad","s-btn","s-btn__link","fs-fine","mt2","float-right"),t.append(document.createTextNode(this.cam.opt.adReportText)),t.removeEventListener("click",this.callOnButtonClick),t.addEventListener("click",this.callOnButtonClick),t}async loadModal(url,$link,googleEventData){try{await window.StackExchange.helpers.loadModal(url,{returnElements:window.$($link)}),this.initForm(googleEventData)}catch(e){var message="",response=e.responseText?eval(`(${e.responseText})`):null;message=response&&response.isLoggedOut?this.cam.opt.adReportLoginExpiredMessage:this.cam.opt.adReportLoginErrorMessage,window.StackExchange.helpers.showToast(message,{type:"danger"})}}removeModal(){window.StackExchange.helpers.closePopups(document.querySelectorAll("."+this.cam.opt.adReportModalClass),"dismiss")}initForm(e,t=!1){this.ignoreValidation=t,this.$form=document.querySelector(".js-ad-report-form"),this.$googleEventData=this.$form.querySelector(".js-json-data"),this.$adReportReasons=this.$form.querySelectorAll(".js-ad-report-reason"),this.$adReportReasonOther=this.$form.querySelector(".js-ad-report-reason-other"),this.$fileUploaderInput=this.$form.querySelector(".js-file-uploader-input"),this.$imageUploader=this.$form.querySelector(".js-image-uploader"),this.$clearImageUpload=this.$form.querySelector(".js-clear-image-upload"),this.$imageUploaderText=this.$form.querySelector(".js-image-uploader-text"),this.$imageUploaderPreview=this.$form.querySelector(".js-image-uploader-preview"),this.$fileErrorMessage=this.$form.querySelector(".js-file-error");const s=this.$form.querySelector(".js-drag-drop-enabled"),n=this.$form.querySelector(".js-drag-drop-disabled");this.$googleEventData.value=e,this.$adReportReasons.forEach((e,t)=>e.addEventListener("change",e=>{this.$adReportReasonOther.classList.toggle("d-none","3"!==e.target.value)})),this.$fileUploaderInput.addEventListener("change",()=>{this.validateFileInput()&&this.updateImagePreview(this.$fileUploaderInput.files)}),this.$clearImageUpload.addEventListener("click",e=>{e.preventDefault(),this.clearImageUpload()});try{this.$fileUploaderInput[0].value="",this.$imageUploader.addEventListener("dragenter dragover dragleave drop",this.preventDefaults),this.$imageUploader.addEventListener("dragenter dragover",this.handleDragStart),this.$imageUploader.addEventListener("dragleave drop",this.handleDragEnd),this.$imageUploader.addEventListener("drop",this.handleDrop)}catch(e){s.classList.add("d-none"),n.classList.remove("d-none")}this.$form.removeEventListener("",this.handleDragEnd),this.$form.addEventListener("submit",async e=>(e.preventDefault(),this.submitForm(),!1))}clearImageUpload(){this.$fileUploaderInput.value="",this.$imageUploaderPreview.setAttribute("src",""),this.$imageUploaderPreview.classList.add("d-none"),this.$clearImageUpload.classList.add("d-none"),this.$imageUploaderText.classList.remove("d-none"),this.$imageUploader.classList.add("p16","ba","bas-dashed","bc-black-100")}preventDefaults(e){e.preventDefault(),e.stopPropagation()}handleDragStart(e){this.$imageUploader.classList.remove("bas-dashed"),this.$imageUploader.classList.add("bas-solid","bc-black-100")}handleDragEnd(e){this.$imageUploader.classList.remove("bas-solid","bc-black-100"),this.$imageUploader.classList.add("bas-dashed")}handleDrop(e){var t=e.originalEvent.dataTransfer.files;FileReader&&t&&1===t.length&&(this.$fileUploaderInput.files=t,this.validateFileInput()&&this.updateImagePreview(t))}setError(e){this.$fileErrorMessage.parentElement.classList.toggle("has-error",e)}updateImagePreview(e){this.$imageUploader.classList.remove("p16","ba","bas-dashed","bc-black-100"),this.$clearImageUpload.classList.remove("d-none"),this.$imageUploaderText.classList.add("d-none");var t=new FileReader;t.onload=e=>{null!=e.target&&(this.$imageUploaderPreview.setAttribute("src",e.target.result),this.$imageUploaderPreview.classList.remove("d-none"))},t.readAsDataURL(e[0])}validateFileInput(){if(this.ignoreValidation)return!0;const e=this.cam.opt.adReportFileTypeErrorMessage,t=this.cam.opt.adReportFileSizeErrorMessage;if(null==this.$fileUploaderInput.files)return!1;var s=this.$fileUploaderInput.files[0];return null==s?(this.setError(!0),!1):this.allowedFileTypes.indexOf(s.type)<0?(this.$fileErrorMessage.textContent=e,this.$fileErrorMessage.classList.remove("d-none"),this.setError(!0),!1):s.size>2097152?(this.$fileErrorMessage.textContent=t,this.$fileErrorMessage.classList.remove("d-none"),this.setError(!0),!1):(this.$fileErrorMessage.classList.add("d-none"),this.setError(!1),!0)}async gatherDiagnosticInfo(){return{BrowserVersion:await this.getBrowserVersion()}}getElementSource(e){return e.outerHTML}getNestedIFrameElement(e){var t=e.querySelector("iframe");return t.contentDocument?t.contentDocument.documentElement:t.contentWindow.document.documentElement}async getBrowserVersion(){return await navigator.userAgentData.getHighEntropyValues(["fullVersionList"]).then(e=>JSON.stringify(e.fullVersionList))}async submitForm(){if(!this.validateFileInput())return!1;this.$form.querySelector("[type=submit]").setAttribute("disabled","true");var e=JSON.parse(this.$googleEventData.value||"{}");e.Reason=parseInt(this.$form.querySelector(".js-ad-report-reason:checked").value,10),e.Description=this.$adReportReasonOther.value,this.$googleEventData.value=JSON.stringify(e);var t=new FormData(this.$form);if("1"===t.get("shareDiagnosticInfo")){var s=await this.gatherDiagnosticInfo();Object.keys(s).forEach(e=>t.append(e,s[e]))}try{const e=await window.fetch(this.$form.getAttribute("action"),{method:this.$form.getAttribute("method"),body:t,cache:"no-cache"}),s=e.headers.get("content-type")||"",o=await e.text();if(!e.ok)throw new Error("response not valid");if(0===s.indexOf("text/html")){var n=(0,_common_helper__WEBPACK_IMPORTED_MODULE_2__.Bv)(o);const e=n?n.querySelector(".js-modal-content"):null;if(_console__WEBPACK_IMPORTED_MODULE_1__.cM("$popupContent"),_console__WEBPACK_IMPORTED_MODULE_1__.cM(e),!e)throw new Error(`Could not find .js-modal-content in response from ${this.$form.getAttribute("action")}`);document.querySelector(".js-modal-content").replaceWith(e)}else window.StackExchange.helpers.showToast(this.cam.opt.adReportThanksText,{type:"success"}),this.removeModal()}catch(e){window.StackExchange.helpers.showToast(this.cam.opt.adReportErrorText,{type:"danger"})}finally{let e=this.$form.querySelector("[type=submit]");e&&e.removeAttribute("disabled")}}}},276:(e,t,s)=>{function n(...e){}function o(...e){}s.d(t,{cM:()=>n,vU:()=>o})}},__webpack_module_cache__={};function __webpack_require__(e){var t=__webpack_module_cache__[e];if(void 0!==t)return t.exports;var s=__webpack_module_cache__[e]={exports:{}};return __webpack_modules__[e](s,s.exports,__webpack_require__),s.exports}__webpack_require__.d=(e,t)=>{for(var s in t)__webpack_require__.o(t,s)&&!__webpack_require__.o(e,s)&&Object.defineProperty(e,s,{enumerable:!0,get:t[s]})},__webpack_require__.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t);var __webpack_exports__={};(()=>{var e=__webpack_require__(276),t=(e=>(e[e.Above=0]="Above",e[e.Below=1]="Below",e))(t||{});const s=Object.assign({},{"lib":"https://cdn.sstatic.net/clc/js/bundles/gam_loader_script/gam_loader_script.bundle.741.c9e247ea74a3cd0a3f1c.min.js","style":null,"u":null,"wa":true,"kt":2000,"tto":true,"h":"clc.stackoverflow.com","allowed":"^(((talent\\.)?stackoverflow)|(blog\\.codinghorror)|(.*\\.googlesyndication)|(serverfault|askubuntu|superuser)|([^\\.]+\\.stackexchange))\\.com$","wv":true,"al":false,"abd":true,"cpa_liid":[5882654614],"cpa_cid":[138377597667],"dp":false,"tgt_to":1000,"tgt_u":"https://clc.stackoverflow.com/get-user-acct-tgt","tgt_e":true,"tgt_p":100,"dv_enabled":true});var n=__webpack_require__(23),o=__webpack_require__(865),a=__webpack_require__(763);class i{constructor(t,s){this.googletag=t,this.interval=s,e.cM("Ad refresh init. interval: "+s),this.googletag.pubads().addEventListener("impressionViewable",e=>this.onImpressionViewable(e)),e.cM("done enabling ad refresh")}onImpressionViewable(t){var s=t.slot;e.cM("ad refresh - slot "+s.getSlotElementId()+" is viewable, initializing refresh"),this.scheduleRefresh(s)}scheduleRefresh(e){setTimeout(()=>this.refreshAdSlot(e),1e3*this.interval)}static refreshMyAd(t,s){let n=t.pubads().getSlots().find(e=>e.getSlotElementId()===s);n&&(e.cM("refreshMyAd - refreshing ad slot "+s),t.pubads().refresh([n]))}static removeMyAd(t,s){let n=t.pubads().getSlots().find(e=>e.getSlotElementId()===s);n&&(e.cM("removeMyAd - destroying ad slot "+s),t.destroySlots([n]))}refreshAdSlot(t){var s=t.getSlotElementId();this.isElementVisibleInBrowser(s)?(e.cM("refreshing ad slot "+s),googletag.pubads().refresh([t])):(e.cM("refresh skipped this time; ad slot not viewable:"+s),this.scheduleRefresh(t))}isElementVisibleInBrowser(e){var t=document.getElementById(e);if(null!==t){var s=t.getBoundingClientRect();if(s.top>=0&&s.left>=0&&s.bottom<=(window.innerHeight||document.documentElement.clientHeight)&&s.right<=(window.innerWidth||document.documentElement.clientWidth))return!0}return!1}}var r=(e=>(e.Off="Off",e.PreSurvey="PreSurvey",e.Collect="Collect",e.PostSurvey="PostSurvey",e))(r||{});class d{constructor(e,t){this.lineItemImpressions=[],this.surveysIdsCompleted=[],this.lineItemImpressions=e,this.surveysIdsCompleted=t}addImpression(e,t){let s={brandId:e,lineItemId:t,timestamp:new Date};this.lineItemImpressions.push(s)}addBrandSurveyCompleted(e){-1===this.surveysIdsCompleted.indexOf(e)&&this.surveysIdsCompleted.push(e)}getTotalBrandImpressions(){let e=new Map;for(let t of this.lineItemImpressions)if(e.has(t.brandId)){let s=e.get(t.brandId);e.set(t.brandId,s+1)}else e.set(t.brandId,1);return e}getBrandLineItemImpressions(e){let t={};for(let s of this.lineItemImpressions)if(s.brandId==e)if(void 0!==t[s.lineItemId]){let e=t[s.lineItemId];t[s.lineItemId]=e+1}else t[s.lineItemId]=1;return t}}class l{constructor(){this.surveyEngagementLocalStorageKey="clc-survey-engagement"}getBrandSurveyEngagement(){let e=localStorage.getItem(this.surveyEngagementLocalStorageKey);if(null===e)return new d([],[]);let t=JSON.parse(e);return new d(t.lineItemImpressions,t.surveysIdsCompleted)}saveBrandSurveyEngagement(e){let t=JSON.stringify(e);localStorage.setItem(this.surveyEngagementLocalStorageKey,t)}}class c{constructor(){this.surveyRepository=new l}getBrandSurveyEngagement(){return this.surveyRepository.getBrandSurveyEngagement()}recordImpression(e,t){let s=this.getBrandSurveyEngagement();s.addImpression(e,t),this.surveyRepository.saveBrandSurveyEngagement(s)}recordBrandSurveyCompleted(e){let t=this.getBrandSurveyEngagement();t.addBrandSurveyCompleted(e),this.surveyRepository.saveBrandSurveyEngagement(t)}}class g{constructor(t,s){this.googletag=t,this.brandSettings=s,this.brandSlotMap=new Map,this.brandSurveyEngagementService=new c,e.cM("Brand Survey init: "+JSON.stringify(s)),void 0!==s?(this.googletag.pubads().addEventListener("slotRenderEnded",e=>this.handleSlotRendered(e)),this.googletag.pubads().addEventListener("impressionViewable",e=>this.onImpressionViewable(e)),e.cM("done enabling Brand Survey")):e.cM("Brand Survey init: brandSettings is undefined, not initializing")}handleSlotRendered(t){e.cM("Brand Survey - slot rendered - slot:"+JSON.stringify(t.slot.getSlotElementId())+" lineItem: "+t.lineItemId);let s=this.findItemWithId(t.lineItemId);if(null===s||s.mode!==r.Collect)this.brandSlotMap.delete(t.slot.getSlotElementId());else{let e={brandId:s.brandId,lineItemId:t.lineItemId};this.brandSlotMap.set(t.slot.getSlotElementId(),e)}}onImpressionViewable(t){let s=t.slot;if(e.cM("ad - Brand Survey - impression viewable.  Details: "+JSON.stringify(s.getSlotElementId())),e.cM("ad - Brand Survey - slot "+s.getSlotElementId()+" is viewable"),this.brandSlotMap.has(s.getSlotElementId())){let t=this.brandSlotMap.get(s.getSlotElementId());e.cM("Brand Survey - brand "+t.brandId+" is viewable"),this.recordImpression(this.brandSlotMap.get(s.getSlotElementId()))}}recordImpression(t){e.cM("ad - Brand Survey - recording impression for brand "+t.brandId),this.brandSurveyEngagementService.recordImpression(t.brandId,t.lineItemId)}findItemWithId(t){return e.cM("brand settings: "+JSON.stringify(this.brandSettings)),this.brandSettings.find(e=>e.lineItemIds.includes(t))||null}}const p="response-brand-survey-submit|",h="request-brand-survey-metadata|",m="record-metric-on-server|",u="request-dsp-tags",f="response-dsp-tags|";class v{static refreshAdIfBrandSurveyIsDuplicated(e,t,s){if(this.alreadyCompletedThisBrandSurvey(t)){var n=document.getElementById(s).closest(".js-zone-container");i.removeMyAd(e,s),n&&n.remove()}}static alreadyCompletedThisBrandSurvey(e){return(new c).getBrandSurveyEngagement().surveysIdsCompleted.includes(e)}}window.cam=new class{constructor(t=null){if(this.gptImported=!1,this.slotsRenderedEvents=[],this.collapsed={},e.cM("constructor"),this.clc_options=s,window.clcGamLoaderOptions)Object.assign(this,window.clcGamLoaderOptions);else if(void 0===this.opt){let e=window.opt;e&&(this.opt=e)}}init(){if(e.cM("init"),void 0===this.opt)throw new Error("opt not set, required by GAM Loader");e.cM("init brand survey service"),this.getUserMetaPromise=this.getUserMeta(),e.cM("setup message handler"),window.addEventListener("message",e=>{this.onmessage(e)})}handleSlotRenderedNoAdReport(){if(googletag.pubads().addEventListener("slotRenderEnded",e=>this.applyExtraMarginBottom(e)),Array.isArray(this.slotsRenderedEvents))for(var e=0;e<this.slotsRenderedEvents.length;e++)this.applyExtraMarginBottom(this.slotsRenderedEvents[e])}onmessage(t){let s="omni";if(t.data&&("string"==typeof t.data||t.data instanceof String))if(0===t.data.indexOf("get-omni-")){e.cM("Recevied get-omni message, sending back omni");var n=t.source,a=this.opt.omni,i="string"==typeof a?a:"";n.postMessage([s,i,this.opt.perRequestGuid].join("|"),"*")}else if(0===t.data.indexOf("collapse-")){e.cM("Recevied collapse message, collapse ad iframe"),e.cM(t);for(var r=t.source.window,d=document.getElementsByTagName("IFRAME"),l=0;l<d.length;l++){var g=d[l];if(g.contentWindow==r)return void(0,o.wo)(g.parentElement.parentElement.parentElement)}}else if(0===t.data.indexOf("resize|")){e.cM("Recevied resize message, resize ad iframe"),e.cM(t);let s=this._getFrameByEvent(t),n=t.data.indexOf("|")+1,o=t.data.slice(n),a=parseFloat(o)+.5;e.cM("New iframe height "+a),s.height=a.toString(),s.parentElement.style.height=a.toString()+"px"}else if(0===t.data.indexOf("getmarkup|")){let s=t.data.indexOf("|")+1,n=t.data.slice(s);e.cM("Recevied get markup message: "+n);let o=this._getFrameByEvent(t).closest(".everyonelovesstackoverflow");const a=document.createElement("script");a.dataset.adZoneId=o.id,a.src=n,document.body.appendChild(a)}else if(0===t.data.indexOf("window-location|")){let s=t.data.indexOf("|")+1,n=t.data.slice(s);e.cM("Recevied window location message: "+n),n.startsWith("/")||(n="/"+n),window.open(window.location.protocol+"//"+window.location.host+n,"_blank")}else if(0===t.data.indexOf("request-brand-survey-submit|")){let s=t.data.split("|"),n=s[1],o=s[2],a=s[3],i=JSON.parse(a);e.cM(n),e.cM(o),e.cM(a),e.cM("Received brand survey "+n+" response message: "+o);var _=new FormData;for(var b in i)_.append(b,i[b]);let r=this._getFrameByEvent(t);if(v.alreadyCompletedThisBrandSurvey(+n))return e.cM("Already completed this brand survey.  Not submitting duplicate to server."),void r.contentWindow.postMessage("response-brand-survey-submit-duplicate|","*");e.cM("Send the brand survey to the server"),fetch(o,{method:"POST",body:_}).then(e=>e.json()).then(e=>r.contentWindow.postMessage({messageType:p},"*")).catch(e=>r.contentWindow.postMessage({messageType:p},"*"))}else if(0===t.data.indexOf("brand-survey-completed-store|")){let s=t.data.split("|"),n=(s[1],s[2]);if(e.cM("Received brand survey completed store message for survey ID "+n),v.alreadyCompletedThisBrandSurvey(+n))return void e.cM("Already completed this brand survey.  Not recording duplicate locally.");e.cM("Record brand survey completion locally"),(new c).recordBrandSurveyCompleted(+n)}else if(0===t.data.indexOf(h)){let s=t.data.split("|"),n=s[1],o=s[2];e.cM("Received message: request-brand-survey-metadata| with Brand Survey ID "+o);let a=(new c).getBrandSurveyEngagement().getBrandLineItemImpressions(+n),i=JSON.stringify(a),r=this._getFrameByEvent(t);e.cM("sending impression data: "+i),r.contentWindow.postMessage("response-brand-survey-metadata|"+this.opt.responseHash+"|"+this.opt.perRequestGuid+"|"+i+"|"+this.opt.countryCode+"|"+this.opt.qualtricsSurveyData,"*")}else if(0===t.data.indexOf("refresh-if-duplicate-brand-survey|")){let e=t.data.split("|")[1],s=this.getSlotElementIdByEvent(t);v.refreshAdIfBrandSurveyIsDuplicated(googletag,+e,s)}else if(0===t.data.indexOf(m)){e.cM("Received message: record-metric-on-server| with args: "+t.data);let s=t.data.split("|"),n=s[1],o=s[2],a=s[3],i=s[4],r=new FormData;r.append("brandSurveyId",a.toString()),r.append("responseHash",this.opt.responseHash),r.append("perRequestGuid",this.opt.perRequestGuid),r.append("questionNumber",n.toString()),r.append("metricType",i.toString()),fetch(o,{method:"POST",body:r}).then(e=>e.ok).catch(t=>{e.cM("SendMetricToServer: Error sending metric to server: "+t)})}else if(0===t.data.indexOf(u)){e.cM("Received message: request-dsp-tags with args: "+t.data);let s=this._getFrameByEvent(t);if(!this.opt.targeting["so-tag"])return void s.contentWindow.postMessage(f,"*");const n=this.opt.targeting["so-tag"].join(",");e.cM("sending targeting tags: "+n),s.contentWindow.postMessage(f+n,"*")}else e.cM("Received unhandled message")}getSlotElementIdByEvent(e){let t=this._getFrameByEvent(e).parentElement?.parentElement?.id;return t||""}_getFrameByEvent(e){return Array.from(document.getElementsByTagName("iframe")).filter(t=>t.contentWindow===e.source)[0]}classifyZoneIds(e){const t=e.map(o.Nj).filter(o.yb);return{eligible:t.filter(o.xb).filter(o.pn),ineligible:t.filter(o.xj)}}applyExtraMarginBottom(t){if(t&&t.slot&&!t.isEmpty&&(t.creativeId||t.lineItemId||!t.isEmpty)){var s=t.slot.getSlotElementId();if(s){var o=document.getElementById(s);if(o)if((0,n.eq)(s)){var a=o?.closest(".js-zone-container");a.style.marginBottom="24px",e.cM("Applied extra margin to the bottom of "+s)}else e.cM("Not applying extra margin to the bottom of "+s+": shouldHaveReportButton = false");else e.cM("Not applying extra margin to the bottom of "+s+": resolved invalid adUnit element")}else e.cM("Not applying extra margin to the bottom of element: invalid adUnitElementId")}else e.cM("Not applying extra margin to the bottom of element: invalid SlotRenderEndedEvent")}async load(s=(0,n.kG)()){const r=this.opt.tlb_position===t.Above?["dfp-mlb","dfp-smlb"]:["dfp-mlb","dfp-smlb","dfp-tlb"];if(!this.isGptReady())return e.cM("Initializing..."),this.initGpt(),void googletag.cmd.push(()=>this.load(s));this.opt.adReportEnabled?(e.cM("Ad reporting enabled"),this.adReports=new a.t(googletag,this)):(e.cM("Ad reporting not enabled"),this.handleSlotRenderedNoAdReport()),this.opt.refresh?(e.cM("Ad refresh enabled"),this.adRefresh=new i(googletag,this.opt.refreshInterval)):e.cM("Ad refresh not enabled"),this.opt.brandSurveyEnabled&&(e.cM("Brand Survey enabled"),this.brandSurvey=new g(googletag,this.opt.brandSurveySettings)),e.cM("Attempting to load ads into ids: ",s);const{eligible:d,ineligible:l}=this.classifyZoneIds(s);if(this.initDebugPanel(googletag,d.concat(l)),d.forEach(e=>(0,o.cf)(e)),l.forEach(o.wo),0===d.length)return void e.cM("Found no ad ids on page");e.cM("Eligible ids:",d),this.opt.abd&&this.appendAdblockDetector();var c=googletag.pubads().getSlots();if(c){var p=c.filter(e=>s.indexOf(e.getSlotElementId())>=0);googletag.destroySlots(p)}this.opt.sf&&(googletag.pubads().setForceSafeFrame(!0),googletag.pubads().setSafeFrameConfig({allowOverlayExpansion:!0,allowPushExpansion:!0,sandbox:!0})),e.cM("Targeting consent: Checking...");let h=!1,m=!1;void 0!==this.opt.targeting_consent&&(m=!0,e.cM("Targeting consent: Parameter set"),e.cM("Targeting consent: Consent given? ",this.opt.targeting_consent),h=this.opt.targeting_consent),void 0!==this.opt.personalization_consent&&(e.cM("Personalization consent: Parameter set"),e.cM("Personalization consent: Consent given? ",this.opt.personalization_consent),h=h&&this.opt.personalization_consent),h=h&&m,this.setPrivacySettings(h),this.opt.ll||googletag.pubads().enableSingleRequest(),cam.sreEvent||(googletag.pubads().addEventListener("slotRenderEnded",e=>this.onSlotRendered(e)),cam.sreEvent=!0),await this.setTargeting();var u=d.filter(e=>!this.opt.ll||r.indexOf(e.id)<0),f=d.filter(e=>!!this.opt.ll&&r.indexOf(e.id)>=0);e.cM("Up front ids:",u),e.cM("Lazy loaded ids:",f),u.forEach(t=>{e.cM(`Defining ad for element ${t.id}`),this.defineSlot(t.id,googletag),t.setAttribute("data-dfp-zone","true")}),googletag.enableServices(),u.forEach(t=>{e.cM(`Displaying ad for element ${t.id}`),this.clc_options.dv_enabled?window.onDvtagReady(function(){googletag.display(t.id)}):googletag.cmd.push(()=>googletag.display(t.id))}),this.opt.ll&&(e.cM("Enabling lazy loading for GAM"),googletag.pubads().enableLazyLoad({fetchMarginPercent:0,renderMarginPercent:0}),e.cM("Setting up lazy loaded ad units"),f.forEach(t=>{e.cM(`Lazy loading - Defining Slot ${t.id}`),this.defineSlot(t.id,googletag)}),f.forEach(t=>{e.cM(`Lazy loading - Displaying ad for element ${t.id}`),this.clc_options.dv_enabled?window.onDvtagReady(function(){googletag.display(t.id)}):googletag.cmd.push(()=>googletag.display(t.id))}))}setPrivacySettings(e){e||googletag.pubads().setPrivacySettings({nonPersonalizedAds:!0})}async setTargeting(){if(!googletag)throw new Error("googletag not defined");let t=this.opt.targeting;if(!t)throw new Error("Targeting not defined (is "+typeof t+")");Object.keys(t).forEach(s=>{e.cM(`-> targeting - ${s}: ${t[s]}`),googletag.pubads().setTargeting(s,t[s])});let s=!1;if(void 0!==this.opt.targeting_consent&&(s=this.opt.targeting_consent),s){let t=(new c).getBrandSurveyEngagement();if(t.getTotalBrandImpressions().forEach((t,s)=>{e.cM(`-> targeting - BrandImpressions: ${s}: ${t}`),googletag.pubads().setTargeting("brand_"+s.toString()+"_impressions",t.toString())}),t.surveysIdsCompleted.forEach(t=>{e.cM(`-> targeting - SurveysTaken: ${t}`),googletag.pubads().setTargeting("survey_"+t+"_taken","true")}),this.clc_options.tgt_e&&this.getUserMetaPromise){let t=await this.getUserMetaPromise;t&&t.tgt_acct?(e.cM("-> targeting - User Account: "+t.tgt_acct),googletag.pubads().setTargeting("user-acct",t.tgt_acct.company_name),googletag.pubads().setTargeting("user_acct_top",t.tgt_acct.company_name),googletag.pubads().setTargeting("user_industry",t.tgt_acct.industry),googletag.pubads().setTargeting("user_employee_count",t.tgt_acct.employee_range)):e.cM("-> targeting - User Account: Not Found"),t&&Object.prototype.hasOwnProperty.call(t,"is_high_rep_earner")?(e.cM("-> targeting - High Rep Earner: "+t.is_high_rep_earner),googletag.pubads().setTargeting("IsHighRepEarner",t.is_high_rep_earner?"true":"false")):e.cM("-> targeting - High Rep Earner: not found")}if(localStorage){e.cM('Checking local storage for "jobs-last-clicked" key.');let t=localStorage.getItem("jobs-last-clicked")?"true":"false";e.cM(`-> targeting - jobs_clicked: ${t}`),googletag.pubads().setTargeting("jobs_clicked",t)}}}appendAdblockDetector(){const e=document.createElement("div");e.className="adsbox",e.id="clc-abd",e.style.position="absolute",e.style.pointerEvents="none",e.innerHTML="&nbsp;",document.body.appendChild(e)}onSlotRendered(s){try{const i=s.slot.getSlotElementId();let r=[];i||r.push("id=0");const d=document.getElementById(i);if(i&&!d&&r.push("el=0"),0!==r.length)return void this.stalled(r.join("&"));const{path:l,sizes:c,zone:g}=(0,n.Z7)(i);if(this.collapsed[g]&&s.isEmpty)return e.cM(`No line item for the element #${d.id}... collapsing.`),void(0,o.wo)(d);if(this.slotsRenderedEvents.push(s),s.lineItemId||s.creativeId||!s.isEmpty){e.cM(`Rendered ad for element #${d.id} [line item #${s.lineItemId}]`),e.cM(s);var a=d.parentElement;if(a.classList.contains("js-zone-container")){switch((0,o.cf)(a),i){case"dfp-tlb":this.opt.tlb_position===t.Above?a.classList.add("mb8"):a.classList.add("mt16");break;case"dfp-tag":a.classList.add("mb8");break;case"dfp-msb":a.classList.add("mt16");break;case"dfp-mlb":case"dfp-smlb":case"dfp-bmlb":a.classList.add("my8");break;case"dfp-isb":a.classList.add("mt24");break;case"dfp-m-aq":a.classList.add("my12"),a.classList.add("mx-auto")}(0,o.$Z)(a),(0,o.$Z)(d)}else e.cM(`No ad for element #${d.id}, collapsing`),e.cM(s),(0,o.wo)(d)}}catch(t){e.cM("Exception thrown onSlotRendered"),e.cM(t),this.stalled("e=1")}}stalled(e){(new Image).src=`https://${this.clc_options.h}/stalled.gif?${e}`}defineSlot(t,s){"dfp-isb"===t&&(e.cM("-> targeting - Sidebar: Inline"),s.pubads().setTargeting("Sidebar",["Inline"])),"dfp-tsb"===t&&(e.cM("-> targeting - Sidebar: Right"),s.pubads().setTargeting("Sidebar",["Right"]));const{path:o,sizes:a,zone:i}=(0,n.Z7)(t);e.cM(`Defining slot for ${t}: ${o}, sizes: ${JSON.stringify(a)}`),s.defineSlot(o,a,t).addService(s.pubads())}importGptLibrary(){this.gptImported||(this.gptImported=!0,void 0===this.opt.targeting_consent||this.opt.targeting_consent?(0,o.Gx)("https://securepubads.g.doubleclick.net/tag/js/gpt.js"):(0,o.Gx)("https://pagead2.googlesyndication.com/tag/js/gpt.js"))}importDvLibrary(){this.clc_options.dv_enabled&&(e.cM("Adding DoubleVerify library"),(0,o.Gx)("https://pub.doubleverify.com/dvtag/21569774/DV1289064/pub.js"),e.cM("Adding DoubleVerify onDvtagReady handler"),window.onDvtagReady=function(t,s=750){e.cM("DoubleVerify onDvtagReady called"),window.dvtag=window.dvtag||{},dvtag.cmd=dvtag.cmd||[];const n={callback:t,timeout:s,timestamp:(new Date).getTime()};dvtag.cmd.push(function(){dvtag.queueAdRequest(n)}),setTimeout(function(){const e=n.callback;n.callback=null,e&&e()},s)})}isGptReady(){return"undefined"!=typeof googletag&&!!googletag.apiReady}initGpt(){"undefined"==typeof googletag&&(window.googletag={cmd:(0,o.QZ)(()=>{this.importGptLibrary(),this.importDvLibrary()})})}getUserMeta(){if(this.opt.allowAccountTargetingForThisRequest&&this.clc_options.tgt_e&&this.clc_options.tgt_p>0){if(e.cM("Targeting enabled."),this.clc_options.tgt_p<100){e.cM("Targeting rate limit enabled.  Rolling the dice...");const t=Math.floor(100*Math.random())+1;if(e.cM("Rolled "+t+" and the max is "+this.clc_options.tgt_p),t>this.clc_options.tgt_p)return void e.cM("Will not request targeting.")}return e.cM("Will request targeting."),function(e,t,s,n){if(t){const t=new Headers;return t.append("Accept","application/json"),async function(e,t={},s=5e3){if("number"!=typeof s&&null!=s&&!1!==s){if("string"!=typeof s)throw new Error("fetchWithTimeout: timeout must be a number");if(s=parseInt(s),isNaN(s))throw new Error("fetchWithTimeout: timeout must be a number (or string that can be parsed to a number)")}const n=new AbortController,{signal:o}=n,a=fetch(e,{...t,signal:o}),i=setTimeout(()=>n.abort(),s);try{const e=await a;return clearTimeout(i),e}catch(e){throw clearTimeout(i),e}}(s+"?"+new URLSearchParams({omni:e}),{method:"GET",mode:"cors",headers:t},n).then(e=>e.json())}return Promise.reject("No consent")}(this.opt.omni,this.opt.targeting_consent,this.clc_options.tgt_u,this.clc_options.tgt_to).catch(t=>{e.vU("Error fetching user account targeting"),e.vU(t)})}e.cM("Targeting disabled.  Will not request account targeting data.")}initDebugPanel(t,s){e.cM("initDebugPanel"),e.cM("Not showing debug panel.")}},window.clcGamLoaderOptions&&(cam.init(),cam.load())})()})();</script>
            
        <footer id="footer" class="site-footer js-footer theme-light__forced" role="contentinfo">
            <div class="site-footer--container">
                    <div class="site-footer--logo">
    
                        <a href="https://stackoverflow.com" aria-label="Stack Overflow"><svg aria-hidden="true" class="native svg-icon iconLogoGlyphMd" width="32" height="37" viewBox="0 0 32 37"><path d="M26 33v-9h4v13H0V24h4v9h22Z" fill="#BCBBBB"/><path d="m21.5 0-2.7 2 9.9 13.3 2.7-2L21.5 0ZM26 18.4 13.3 7.8l2.1-2.5 12.7 10.6-2.1 2.5ZM9.1 15.2l15 7 1.4-3-15-7-1.4 3Zm14 10.79.68-2.95-16.1-3.35L7 23l16.1 2.99ZM23 30H7v-3h16v3Z" fill="#F48024"/></svg></a>
                    </div>
                <nav class="site-footer--nav">
                        <div class="site-footer--col">
                            <h5 class="-title"><a href="https://stackoverflow.com" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 15})">Stack Overflow</a></h5>
                            <ul class="-list js-primary-footer-links">
                                <li><a href="/questions" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 16})">Questions</a></li>
                                    <li><a href="/help" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 3 })">Help</a></li>
                            </ul>
                        </div>
                        <div class="site-footer--col">
                            <h5 class="-title"><a href="https://stackoverflow.co/" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 19 })">Products</a></h5>
                            <ul class="-list">
                                <li><a href="https://stackoverflow.co/teams/" class="js-gps-track -link"
                                                     data-ga="[&quot;teams traffic&quot;,&quot;footer - site nav&quot;,&quot;stackoverflow.com/teams&quot;,null,{&quot;dimension4&quot;:&quot;teams&quot;}]"
                                                     data-gps-track="footer.click({ location: 2, link: 29 })">Teams</a></li>
                                <li><a href="https://stackoverflow.co/advertising/" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 21 })">Advertising</a></li>
                                <li><a href="https://stackoverflow.co/collectives/" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 40 })">Collectives</a></li>
                                <li><a href="https://stackoverflow.co/talent/" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 20 })">Talent</a></li>
                            </ul>
                        </div>
                    <div class="site-footer--col">
                        <h5 class="-title"><a class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.co/">Company</a></h5>
                        <ul class="-list">
                                <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.co/">About</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 27 })" href="https://stackoverflow.co/company/press/">Press</a></li>
                                <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 9 })" href="https://stackoverflow.co/company/work-here/">Work Here</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 7 })" href="https://stackoverflow.com/legal">Legal</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 8 })" href="https://stackoverflow.com/legal/privacy-policy">Privacy Policy</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 37 })" href="https://stackoverflow.com/legal/terms-of-service/public">Terms of Service</a></li>
                                <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 13 })" href="/contact">Contact Us</a></li>
                                <li id="consent-footer-link"><button type="button" data-controller="cookie-settings" data-action="click->cookie-settings#toggle" class="s-btn s-btn__link py4 js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 38 })" data-consent-popup-loader="footer">Cookie Settings</button></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 39 })" href="https://stackoverflow.com/legal/cookie-policy">Cookie Policy</a></li>
                        </ul>
                    </div>
                    <div class="site-footer--col site-footer--categories-nav">
                        <div>
                            <h5 class="-title"><a href="https://stackexchange.com" data-gps-track="footer.click({ location: 2, link: 30 })">Stack Exchange Network</a></h5>
                            <ul class="-list">
                                <li>
                                    <a href="https://stackexchange.com/sites#technology" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                        Technology
                                    </a>
                                </li>
                                <li>
                                    <a href="https://stackexchange.com/sites#culturerecreation" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                        Culture &amp; recreation
                                    </a>
                                </li>
                                <li>
                                    <a href="https://stackexchange.com/sites#lifearts" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                        Life &amp; arts
                                    </a>
                                </li>
                                <li>
                                    <a href="https://stackexchange.com/sites#science" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                        Science
                                    </a>
                                </li>
                                <li>
                                    <a href="https://stackexchange.com/sites#professional" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                        Professional
                                    </a>
                                </li>
                                <li>
                                    <a href="https://stackexchange.com/sites#business" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                        Business
                                    </a>
                                </li>
    
                                <li class="mt16 md:mt0">
                                    <a href="https://api.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                        API
                                    </a>
                                </li>
    
                                <li>
                                    <a href="https://data.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                        Data
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                <div class="site-footer--copyright fs-fine md:mt24">
                    <ul class="-list -social md:mb8">
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link:4 })" href="https://stackoverflow.blog?blb=1">Blog</a></li>
                        <li><a href="https://www.facebook.com/officialstackoverflow/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 31 })">Facebook</a></li>
                        <li><a href="https://twitter.com/stackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 32 })">Twitter</a></li>
                        <li><a href="https://linkedin.com/company/stack-overflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 33 })">LinkedIn</a></li>
                        <li><a href="https://www.instagram.com/thestackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 36 })">Instagram</a></li>
                    </ul>
    
                    <p class="md:mb0">
    Site design / logo &#169; 2024 Stack Exchange Inc; user contributions licensed under <span class='td-underline'><a href="https://stackoverflow.com/help/licensing">CC BY-SA</a></span>.                    <span id="svnrev">rev&nbsp;2024.5.14.9053</span>
                    </p>
                </div>
            </div>
    
        </footer>
    
    
        
    
                <!-- Google tag (gtag.js) -->
                <script async src="https://www.googletagmanager.com/gtag/js?id=G-WCZ03SZFCQ"></script>
                <script>
                    window.dataLayer = window.dataLayer || [];
                    function gtag() { dataLayer.push(arguments); }
                </script>
                <script>
                    (function(i, s, o, g, r, a, m) {
                        i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function() { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o),
                            m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m);
                    })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');
                </script>
            <script>
                StackExchange.ready(function() {
    
                    var ga3Settings = {
                        autoLink: ["stackoverflow.blog","info.stackoverflowsolutions.com","stackoverflowsolutions.com"],
                        sendTitles: true,
                        tracker: window.ga,
                        trackingCodes: [
                            'UA-108242619-1'
                        ],
                        checkDimension: 'dimension42'
                    };
    
                    var customGA4Dimensions = {};
    
    
                    customGA4Dimensions["requestid"] = "fe709cfc-caf4-4ee3-af7b-ab22ccef65a2";
    
                        customGA4Dimensions["routename"] = "Questions/Show";
    
    
                        customGA4Dimensions["post_id"] = "64159777";
    
    
                        customGA4Dimensions["tags"] = "|tensorflow|keras|neural-network|lstm|lstm-stateful|";
    
    
                    var ga4Settings = {
                        tracker: gtag,
                        trackingCodes: [
                            'G-WCZ03SZFCQ'
                        ],
                        consentsToPerformanceCookies: "granted",
                        consentsToTargetingCookies: "granted",
                        eventParameters: customGA4Dimensions,
                        checkForAdBlock: true,
                        sendTitles: true,
                        trackClicks: false,
                    };
    
                    StackExchange.ga.init({ GA3: ga3Settings, GA4: ga4Settings });
    
    
                    StackExchange.ga.setDimension('dimension2', '|tensorflow|keras|neural-network|lstm|lstm-stateful|');
    
    
                    StackExchange.ga.setDimension('dimension3', 'Questions/Show');
    
    
                    StackExchange.ga.setDimension('dimension7', "1715767546.958501537");
    
                    StackExchange.ga.trackPageView();
                });
            </script>
            
                <script src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js" charset="UTF-8" data-document-language="true" data-domain-script="c3d9f1e3-55f3-4eba-b268-46cee4c6789c"></script>
    <script defer src="https://cdn.sstatic.net/Js/modules/cookie-consent.en.js?v=36bebc18e04f"></script>
    
        
        </body>
        </html>
    """

# Parse the HTML
root = etree.HTML(html)

# Select the element you want to generate XPath for
element = root.xpath("//input")[0]  # Selecting the first paragraph element

# Generate XPath for the selected element
xpath = generate_xpath(element)
print("XPath:", xpath)