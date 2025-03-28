[Skip to content](https://fastapi.tiangolo.com/reference/openapi/docs/#openapi-docs)

# OpenAPI `docs` [¶](https://fastapi.tiangolo.com/reference/openapi/docs/\#openapi-docs "Permanent link")

Utilities to handle OpenAPI automatic UI documentation, including Swagger UI (by default at `/docs`) and ReDoc (by default at `/redoc`).

## `` fastapi.openapi.docs.get\_swagger\_ui\_html [¶](https://fastapi.tiangolo.com/reference/openapi/docs/\#fastapi.openapi.docs.get_swagger_ui_html "Permanent link")

```md-code__content
get_swagger_ui_html(
    *,
    openapi_url,
    title,
    swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
    swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
    oauth2_redirect_url=None,
    init_oauth=None,
    swagger_ui_parameters=None
)

```

Generate and return the HTML that loads Swagger UI for the interactive
API docs (normally served at `/docs`).

You would only call this function yourself if you needed to override some parts,
for example the URLs to use to load Swagger UI's JavaScript and CSS.

Read more about it in the
[FastAPI docs for Configure Swagger UI](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/)
and the [FastAPI docs for Custom Docs UI Static Assets (Self-Hosting)](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/).

| PARAMETER | DESCRIPTION |
| --- | --- |
| `openapi_url` | The OpenAPI URL that Swagger UI should load and use.<br>This is normally done automatically by FastAPI using the default URL<br>`/openapi.json`.<br>**TYPE:** `str` |
| `title` | The HTML `<title>` content, normally shown in the browser tab.<br>**TYPE:** `str` |
| `swagger_js_url` | The URL to use to load the Swagger UI JavaScript.<br>It is normally set to a CDN URL.<br>**TYPE:** `str`**DEFAULT:** `'https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js'` |
| `swagger_css_url` | The URL to use to load the Swagger UI CSS.<br>It is normally set to a CDN URL.<br>**TYPE:** `str`**DEFAULT:** `'https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css'` |
| `swagger_favicon_url` | The URL of the favicon to use. It is normally shown in the browser tab.<br>**TYPE:** `str`**DEFAULT:** `'https://fastapi.tiangolo.com/img/favicon.png'` |
| `oauth2_redirect_url` | The OAuth2 redirect URL, it is normally automatically handled by FastAPI.<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `init_oauth` | A dictionary with Swagger UI OAuth2 initialization configurations.<br>**TYPE:** `Optional[Dict[str, Any]]`**DEFAULT:** `None` |
| `swagger_ui_parameters` | Configuration parameters for Swagger UI.<br>It defaults to [swagger\_ui\_default\_parameters](https://fastapi.tiangolo.com/reference/openapi/docs/#fastapi.openapi.docs.swagger_ui_default_parameters "<code class=\"doc-symbol doc-symbol-heading doc-symbol-attribute\"></code>            <span class=\"doc doc-object-name doc-attribute-name\">fastapi.openapi.docs.swagger_ui_default_parameters</span>     <span class=\"doc doc-labels\">       <small class=\"doc doc-label doc-label-module-attribute\"><code>module-attribute</code></small>   </span>").<br>**TYPE:** `Optional[Dict[str, Any]]`**DEFAULT:** `None` |

Source code in `fastapi/openapi/docs.py`

|     |     |
| --- | --- |
| ```<br> 26<br> 27<br> 28<br> 29<br> 30<br> 31<br> 32<br> 33<br> 34<br> 35<br> 36<br> 37<br> 38<br> 39<br> 40<br> 41<br> 42<br> 43<br> 44<br> 45<br> 46<br> 47<br> 48<br> 49<br> 50<br> 51<br> 52<br> 53<br> 54<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>``` | ```md-code__content<br>def get_swagger_ui_html(<br>    *,<br>    openapi_url: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The OpenAPI URL that Swagger UI should load and use.<br>            This is normally done automatically by FastAPI using the default URL<br>            `/openapi.json`.<br>            """<br>        ),<br>    ],<br>    title: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The HTML `<title>` content, normally shown in the browser tab.<br>            """<br>        ),<br>    ],<br>    swagger_js_url: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The URL to use to load the Swagger UI JavaScript.<br>            It is normally set to a CDN URL.<br>            """<br>        ),<br>    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",<br>    swagger_css_url: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The URL to use to load the Swagger UI CSS.<br>            It is normally set to a CDN URL.<br>            """<br>        ),<br>    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",<br>    swagger_favicon_url: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The URL of the favicon to use. It is normally shown in the browser tab.<br>            """<br>        ),<br>    ] = "https://fastapi.tiangolo.com/img/favicon.png",<br>    oauth2_redirect_url: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            The OAuth2 redirect URL, it is normally automatically handled by FastAPI.<br>            """<br>        ),<br>    ] = None,<br>    init_oauth: Annotated[<br>        Optional[Dict[str, Any]],<br>        Doc(<br>            """<br>            A dictionary with Swagger UI OAuth2 initialization configurations.<br>            """<br>        ),<br>    ] = None,<br>    swagger_ui_parameters: Annotated[<br>        Optional[Dict[str, Any]],<br>        Doc(<br>            """<br>            Configuration parameters for Swagger UI.<br>            It defaults to [swagger_ui_default_parameters][fastapi.openapi.docs.swagger_ui_default_parameters].<br>            """<br>        ),<br>    ] = None,<br>) -> HTMLResponse:<br>    """<br>    Generate and return the HTML  that loads Swagger UI for the interactive<br>    API docs (normally served at `/docs`).<br>    You would only call this function yourself if you needed to override some parts,<br>    for example the URLs to use to load Swagger UI's JavaScript and CSS.<br>    Read more about it in the<br>    [FastAPI docs for Configure Swagger UI](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/)<br>    and the [FastAPI docs for Custom Docs UI Static Assets (Self-Hosting)](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/).<br>    """<br>    current_swagger_ui_parameters = swagger_ui_default_parameters.copy()<br>    if swagger_ui_parameters:<br>        current_swagger_ui_parameters.update(swagger_ui_parameters)<br>    html = f"""<br>    <!DOCTYPE html><br>    <html><br>    <head><br>    <link type="text/css" rel="stylesheet" href="{swagger_css_url}"><br>    <link rel="shortcut icon" href="{swagger_favicon_url}"><br>    <title>{title}</title><br>    </head><br>    <body><br>    <div id="swagger-ui"><br>    </div><br>    <script src="{swagger_js_url}"></script><br>    <!-- `SwaggerUIBundle` is now available on the page --><br>    <script><br>    const ui = SwaggerUIBundle({{<br>        url: '{openapi_url}',<br>    """<br>    for key, value in current_swagger_ui_parameters.items():<br>        html += f"{json.dumps(key)}: {json.dumps(jsonable_encoder(value))},\n"<br>    if oauth2_redirect_url:<br>        html += f"oauth2RedirectUrl: window.location.origin + '{oauth2_redirect_url}',"<br>    html += """<br>    presets: [<br>        SwaggerUIBundle.presets.apis,<br>        SwaggerUIBundle.SwaggerUIStandalonePreset<br>        ],<br>    })"""<br>    if init_oauth:<br>        html += f"""<br>        ui.initOAuth({json.dumps(jsonable_encoder(init_oauth))})<br>        """<br>    html += """<br>    </script><br>    </body><br>    </html><br>    """<br>    return HTMLResponse(html)<br>``` |

## `` fastapi.openapi.docs.get\_redoc\_html [¶](https://fastapi.tiangolo.com/reference/openapi/docs/\#fastapi.openapi.docs.get_redoc_html "Permanent link")

```md-code__content
get_redoc_html(
    *,
    openapi_url,
    title,
    redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js",
    redoc_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
    with_google_fonts=True
)

```

Generate and return the HTML response that loads ReDoc for the alternative
API docs (normally served at `/redoc`).

You would only call this function yourself if you needed to override some parts,
for example the URLs to use to load ReDoc's JavaScript and CSS.

Read more about it in the
[FastAPI docs for Custom Docs UI Static Assets (Self-Hosting)](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/).

| PARAMETER | DESCRIPTION |
| --- | --- |
| `openapi_url` | The OpenAPI URL that ReDoc should load and use.<br>This is normally done automatically by FastAPI using the default URL<br>`/openapi.json`.<br>**TYPE:** `str` |
| `title` | The HTML `<title>` content, normally shown in the browser tab.<br>**TYPE:** `str` |
| `redoc_js_url` | The URL to use to load the ReDoc JavaScript.<br>It is normally set to a CDN URL.<br>**TYPE:** `str`**DEFAULT:** `'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'` |
| `redoc_favicon_url` | The URL of the favicon to use. It is normally shown in the browser tab.<br>**TYPE:** `str`**DEFAULT:** `'https://fastapi.tiangolo.com/img/favicon.png'` |
| `with_google_fonts` | Load and use Google Fonts.<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/openapi/docs.py`

|     |     |
| --- | --- |
| ```<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>197<br>198<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>208<br>209<br>210<br>211<br>212<br>213<br>214<br>215<br>216<br>217<br>218<br>219<br>220<br>221<br>222<br>223<br>224<br>225<br>226<br>227<br>228<br>229<br>230<br>231<br>232<br>233<br>234<br>235<br>236<br>237<br>238<br>239<br>240<br>241<br>242<br>243<br>244<br>245<br>246<br>247<br>248<br>249<br>250<br>251<br>252<br>253<br>``` | ```md-code__content<br>def get_redoc_html(<br>    *,<br>    openapi_url: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The OpenAPI URL that ReDoc should load and use.<br>            This is normally done automatically by FastAPI using the default URL<br>            `/openapi.json`.<br>            """<br>        ),<br>    ],<br>    title: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The HTML `<title>` content, normally shown in the browser tab.<br>            """<br>        ),<br>    ],<br>    redoc_js_url: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The URL to use to load the ReDoc JavaScript.<br>            It is normally set to a CDN URL.<br>            """<br>        ),<br>    ] = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js",<br>    redoc_favicon_url: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The URL of the favicon to use. It is normally shown in the browser tab.<br>            """<br>        ),<br>    ] = "https://fastapi.tiangolo.com/img/favicon.png",<br>    with_google_fonts: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            Load and use Google Fonts.<br>            """<br>        ),<br>    ] = True,<br>) -> HTMLResponse:<br>    """<br>    Generate and return the HTML response that loads ReDoc for the alternative<br>    API docs (normally served at `/redoc`).<br>    You would only call this function yourself if you needed to override some parts,<br>    for example the URLs to use to load ReDoc's JavaScript and CSS.<br>    Read more about it in the<br>    [FastAPI docs for Custom Docs UI Static Assets (Self-Hosting)](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/).<br>    """<br>    html = f"""<br>    <!DOCTYPE html><br>    <html><br>    <head><br>    <title>{title}</title><br>    <!-- needed for adaptive design --><br>    <meta charset="utf-8"/><br>    <meta name="viewport" content="width=device-width, initial-scale=1"><br>    """<br>    if with_google_fonts:<br>        html += """<br>    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet"><br>    """<br>    html += f"""<br>    <link rel="shortcut icon" href="{redoc_favicon_url}"><br>    <!--<br>    ReDoc doesn't change outer page styles<br>    --><br>    <style><br>      body {{<br>        margin: 0;<br>        padding: 0;<br>      }}<br>    </style><br>    </head><br>    <body><br>    <noscript><br>        ReDoc requires Javascript to function. Please enable it to browse the documentation.<br>    </noscript><br>    <redoc spec-url="{openapi_url}"></redoc><br>    <script src="{redoc_js_url}"> </script><br>    </body><br>    </html><br>    """<br>    return HTMLResponse(html)<br>``` |

## `` fastapi.openapi.docs.get\_swagger\_ui\_oauth2\_redirect\_html [¶](https://fastapi.tiangolo.com/reference/openapi/docs/\#fastapi.openapi.docs.get_swagger_ui_oauth2_redirect_html "Permanent link")

```md-code__content
get_swagger_ui_oauth2_redirect_html()

```

Generate the HTML response with the OAuth2 redirection for Swagger UI.

You normally don't need to use or change this.

Source code in `fastapi/openapi/docs.py`

|     |     |
| --- | --- |
| ```<br>256<br>257<br>258<br>259<br>260<br>261<br>262<br>263<br>264<br>265<br>266<br>267<br>268<br>269<br>270<br>271<br>272<br>273<br>274<br>275<br>276<br>277<br>278<br>279<br>280<br>281<br>282<br>283<br>284<br>285<br>286<br>287<br>288<br>289<br>290<br>291<br>292<br>293<br>294<br>295<br>296<br>297<br>298<br>299<br>300<br>301<br>302<br>303<br>304<br>305<br>306<br>307<br>308<br>309<br>310<br>311<br>312<br>313<br>314<br>315<br>316<br>317<br>318<br>319<br>320<br>321<br>322<br>323<br>324<br>325<br>326<br>327<br>328<br>329<br>330<br>331<br>332<br>333<br>334<br>335<br>336<br>337<br>338<br>339<br>340<br>341<br>342<br>343<br>344<br>``` | ```md-code__content<br>def get_swagger_ui_oauth2_redirect_html() -> HTMLResponse:<br>    """<br>    Generate the HTML response with the OAuth2 redirection for Swagger UI.<br>    You normally don't need to use or change this.<br>    """<br>    # copied from https://github.com/swagger-api/swagger-ui/blob/v4.14.0/dist/oauth2-redirect.html<br>    html = """<br>    <!doctype html><br>    <html lang="en-US"><br>    <head><br>        <title>Swagger UI: OAuth2 Redirect</title><br>    </head><br>    <body><br>    <script><br>        'use strict';<br>        function run () {<br>            var oauth2 = window.opener.swaggerUIRedirectOauth2;<br>            var sentState = oauth2.state;<br>            var redirectUrl = oauth2.redirectUrl;<br>            var isValid, qp, arr;<br>            if (/code|token|error/.test(window.location.hash)) {<br>                qp = window.location.hash.substring(1).replace('?', '&');<br>            } else {<br>                qp = location.search.substring(1);<br>            }<br>            arr = qp.split("&");<br>            arr.forEach(function (v,i,_arr) { _arr[i] = '"' + v.replace('=', '":"') + '"';});<br>            qp = qp ? JSON.parse('{' + arr.join() + '}',<br>                    function (key, value) {<br>                        return key === "" ? value : decodeURIComponent(value);<br>                    }<br>            ) : {};<br>            isValid = qp.state === sentState;<br>            if ((<br>              oauth2.auth.schema.get("flow") === "accessCode" ||<br>              oauth2.auth.schema.get("flow") === "authorizationCode" ||<br>              oauth2.auth.schema.get("flow") === "authorization_code"<br>            ) && !oauth2.auth.code) {<br>                if (!isValid) {<br>                    oauth2.errCb({<br>                        authId: oauth2.auth.name,<br>                        source: "auth",<br>                        level: "warning",<br>                        message: "Authorization may be unsafe, passed state was changed in server. The passed state wasn't returned from auth server."<br>                    });<br>                }<br>                if (qp.code) {<br>                    delete oauth2.state;<br>                    oauth2.auth.code = qp.code;<br>                    oauth2.callback({auth: oauth2.auth, redirectUrl: redirectUrl});<br>                } else {<br>                    let oauthErrorMsg;<br>                    if (qp.error) {<br>                        oauthErrorMsg = "["+qp.error+"]: " +<br>                            (qp.error_description ? qp.error_description+ ". " : "no accessCode received from the server. ") +<br>                            (qp.error_uri ? "More info: "+qp.error_uri : "");<br>                    }<br>                    oauth2.errCb({<br>                        authId: oauth2.auth.name,<br>                        source: "auth",<br>                        level: "error",<br>                        message: oauthErrorMsg || "[Authorization failed]: no accessCode received from the server."<br>                    });<br>                }<br>            } else {<br>                oauth2.callback({auth: oauth2.auth, token: qp, isValid: isValid, redirectUrl: redirectUrl});<br>            }<br>            window.close();<br>        }<br>        if (document.readyState !== 'loading') {<br>            run();<br>        } else {<br>            document.addEventListener('DOMContentLoaded', function () {<br>                run();<br>            });<br>        }<br>    </script><br>    </body><br>    </html><br>        """<br>    return HTMLResponse(content=html)<br>``` |

## `` fastapi.openapi.docs.swagger\_ui\_default\_parameters`module-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/docs/\#fastapi.openapi.docs.swagger_ui_default_parameters "Permanent link")

```md-code__content
swagger_ui_default_parameters = {
    "dom_id": "#swagger-ui",
    "layout": "BaseLayout",
    "deepLinking": True,
    "showExtensions": True,
    "showCommonExtensions": True,
}

```

Default configurations for Swagger UI.

You can use it as a template to add any other configurations needed.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top