--TEST: curl -k --data '{"c":789,"d":012}' https://www.test.3927.com/lua/123/456?a=123
--添加如下内容  
--ngx.say("hello world, this is openresty!");
--ngx.redirect("http://jd.com", 302)
--ngx.status=状态码，设置响应的状态码；
--ngx.resp.get_headers()获取设置的响应状态码；
--ngx.send_headers()发送响应状态码，当调用ngx.say/ngx.print时自动发送响应状态码；
--可以通过ngx.headers_sent=true判断是否发送了响应状态码。
--ngx.escape_uri/ngx.unescape_uri ： uri编码解码；
--ngx.encode_args/ngx.decode_args：参数编码解码；
--ngx.encode_base64/ngx.decode_base64：BASE64编码解码；
--ngx.re.match：nginx正则表达式匹配；
--更多Nginx Lua API请参考 http://wiki.nginx.org/HttpLuaModule#Nginx_API_for_Lua

--nginx变量  
local var = ngx.var  
ngx.say("ngx.var.a : ", var.a, "<br/>")  
ngx.say("ngx.var.b : ", var.b, "<br/>")  
ngx.say("ngx.var[2] : ", var[2], "<br/>")  
ngx.var.b = 2;  
  
ngx.say("<br/>")  
  
--请求头  
local headers = ngx.req.get_headers()  
ngx.say("headers begin", "<br/>")  
ngx.say("Host : ", headers["Host"], "<br/>")  
ngx.say("user-agent : ", headers["user-agent"], "<br/>")  
ngx.say("user-agent : ", headers.user_agent, "<br/>")  
for k,v in pairs(headers) do  
    if type(v) == "table" then  
        ngx.say(k, " : ", table.concat(v, ","), "<br/>")  
    else  
        ngx.say(k, " : ", v, "<br/>")  
    end  
end  
ngx.say("headers end", "<br/>")  
ngx.say("<br/>")  
  
--get请求uri参数  
ngx.say("uri args begin", "<br/>")  
local uri_args = ngx.req.get_uri_args()  
for k, v in pairs(uri_args) do  
    if type(v) == "table" then  
        ngx.say(k, " : ", table.concat(v, ", "), "<br/>")  
    else  
        ngx.say(k, ": ", v, "<br/>")  
    end  
end  
ngx.say("uri args end", "<br/>")  
ngx.say("<br/>")  
  
--post请求参数  
ngx.req.read_body()  
ngx.say("post args begin", "<br/>")  
local post_args = ngx.req.get_post_args()  
for k, v in pairs(post_args) do  
    if type(v) == "table" then  
        ngx.say(k, " : ", table.concat(v, ", "), "<br/>")  
    else  
        ngx.say(k, ": ", v, "<br/>")  
    end  
end  
ngx.say("post args end", "<br/>")  
ngx.say("<br/>")  
  
--请求的http协议版本  
ngx.say("ngx.req.http_version : ", ngx.req.http_version(), "<br/>")  
--请求方法  
ngx.say("ngx.req.get_method : ", ngx.req.get_method(), "<br/>")  
--原始的请求头内容  
ngx.say("ngx.req.raw_header : ",  ngx.req.raw_header(), "<br/>")  
--请求的body内容体  
ngx.say("ngx.req.get_body_data() : ", ngx.req.get_body_data(), "<br/>")  
ngx.say("<br/>")  


--写响应头  
--ngx.header.a = "1"  
--多个响应头可以使用table  
--ngx.header.b = {"2", "3"}  
--输出响应  
--ngx.say("a", "b", "<br/>")  
--ngx.print("c", "d", "<br/>")  
--200状态码退出  
--return ngx.exit(200)  


