/* This query will generate an event that deletes stale audit rows
yearly till dec 31,2029
*/

DELIMITER $$
DROP EVENT IF EXISTS yearly_delete_state_audit_rows;
CREATE EVENT yearly_delete_state_audit_rows
ON SCHEDULE
	EVERY 1 YEAR STARTS '2019-01-01' ENDS '2029-12-31'
DO BEGIN
	DELETE FROM payments_audit
    WHERE action_date < NOW() - INTERVAL 1 YEAR;
    -- Another appraoch can be DATESUB(NOW(), INTERVAL 1 YEAR) --
END$$

DELIMITER ;

