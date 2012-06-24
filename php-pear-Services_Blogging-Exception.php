<?php
/**
 * Exception class for the Services_Blogging Drivers.
 * 
 * Extends the Services_Blogging_Exception exception class
 * to make it easyto distinguish between driver and other
 * exceptions via instanceof or in try/catch().
 *
 * @category Services
 * @package  Services_Blogging
 * @author   Anant Narayanan <anant@php.net>
 * @author   Christian Weiske <cweiske@php.net>
 * @license  http://www.gnu.org/copyleft/lesser.html  LGPL License 2.1
 * @link     http://pear.php.net/package/Services_Blogging
 */
require_once 'Services/Blogging/Exception.php';

class Services_Blogging_Driver_Exception
    extends Services_Blogging_Exception
{
}
?>
