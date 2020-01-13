# FB-group-photo-scrape

is there any cookie file
if True ==>> check login
            is check login has user logged
            if True ==>> go to main
            if False ==>> go to login
if False ==>> send login

login ==>> take username & pass then submit
        if password incorrect ==>> send warning
        elif need 2way auth ==>> want pin
        else save browser & cookie for further use
            then goto main func

main ==> need a group url
check url is valid ==>> if not send warning
if valid ==>> check user has joined ==>> if not send warning
else goto 'groupurl/photos'
    then check how much photo it has
    at last download all

